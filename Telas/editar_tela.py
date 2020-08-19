from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from datetime import date
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.label import MDLabel

import json


class Editar_tela(Screen):
    dados_clientes=[]
    novo_cliente={}
    popup_error=None
    popup_certeza=None

        
    def on_pre_enter(self):
        print('Entrando em Editar_tela')
        app = MDApp.get_running_app()
        app.registrar_tela()
        Window.bind(on_keyboard=app.voltar)        
        self.dados_clientes = app.dados_clientes
        self.ids.scroll.scroll_y = 1
        
    
    def adicionar_infos(self,root):
        dados=[]
        print('Adicionando infos a Editar_tela')
        codigo = str(root.ids.info_tab.ids.codigo.text)        
        print('Adicionando informações do cliente:', codigo)
        for cliente in self.dados_clientes:
            if codigo == str(cliente['codigo']):
                dados = cliente

        app = MDApp.get_running_app()
        editar_tela = app.root.get_screen('Editar_tela')
        lista = ['therapet','tesoura','tap_higienico','banho','tosa','pet_shop','clinica']
        #print(type(editar_tela))
        #print(editar_tela)
        #print(editar_tela.ids)
        for campo, _ in editar_tela.ids.items():
            if campo != 'scroll_info':
                try:
                    editar_tela.ids[campo].text = str(dados[campo])
                except KeyError:
                    editar_tela.ids[campo].text = ''
            elif campo in lista:
                try:
                    x = (lambda a: 'True' if a == 'true' else 'False')
                    editar_tela.ids[campo].active = dados[campo]
                except KeyError:
                    editar_tela.ids[campo].active = 'False'
        
        self.endereco = editar_tela.ids['endereco'].text
        self.numero = editar_tela.ids['numero'].text
        self.bairro = editar_tela.ids['bairro'].text
        self.cidade = editar_tela.ids['cidade'].text

           
        
    def abrir_popup_certeza(self):
        if not self.popup_certeza:
            app = MDApp.get_running_app()
            self.popup_certeza = MDDialog( size_hint = [0.8,0.8],
                text="Deseja realizar as alterações?",
                buttons=[
                    MDRaisedButton(
                        text="Sim",text_color=MDApp.get_running_app().theme_cls.text_color, on_release = self.adicionar
                    ),
                    MDFlatButton(
                        text="Não", text_color=MDApp.get_running_app().theme_cls.primary_color, on_release = self.fechar_popup_certeza
                    )
                ],
            )
        self.popup_certeza.open()
    
    def fechar_popup_certeza(self,*args):
        self.popup_certeza.dismiss()
    


    def adicionar(self,*args):
        self.popup_certeza.dismiss()
        novo_cliente={}

        novo_cliente['codigo']         = self.ids.codigo.text
        novo_cliente['nome_fantasia']  = self.ids.nome_fantasia.text
        novo_cliente['endereco']       = self.ids.endereco.text
        novo_cliente['numero']         = self.ids.numero.text
        novo_cliente['bairro']         = self.ids.bairro.text
        novo_cliente['cidade']         = self.ids.cidade.text
        novo_cliente['telefone_fixo']  = self.ids.telefone_fixo.text
        novo_cliente['perfil_cliente'] = self.ids.perfil_cliente.text
        novo_cliente['nome_1']         = self.ids.nome_1.text
        novo_cliente['telefone_1']     = self.ids.telefone_1.text
        novo_cliente['tipo_1']         = self.ids.tipo_1.text
        novo_cliente['nome_2']         = self.ids.nome_2.text
        novo_cliente['telefone_2']     = self.ids.telefone_2.text
        novo_cliente['tipo_2']         = self.ids.tipo_2.text
        novo_cliente['nome_3']         = self.ids.nome_3.text
        novo_cliente['telefone_3']     = self.ids.telefone_3.text
        novo_cliente['tipo_3']         = self.ids.tipo_3.text
        novo_cliente['data']           = str(date.today())
        novo_cliente['razao_social']   = self.ids.razao_social.text
        novo_cliente['cnpj']           = self.ids.cnpj.text
        novo_cliente['cep']            = self.ids.cep.text

        #novo_cliente['lat']           = self.lat
        #novo_cliente['lon']           = self.lon

        novo_cliente['banho']          = self.ids.banho.active
        novo_cliente['tosa']           = self.ids.tosa.active
        novo_cliente['pet_shop']       = self.ids.pet_shop.active
        novo_cliente['clinica']        = self.ids.clinica.active

        novo_cliente['cliente']        = ''
        novo_cliente['therapet']       = ''
        novo_cliente['tesoura']        = ''
        novo_cliente['tap_higienico']  = ''

        
        self.novo_cliente = novo_cliente

        if str(novo_cliente['endereco']) != str(self.endereco) or \
           str(novo_cliente['numero'])   != str(self.numero) or \
           str(novo_cliente['bairro'])   != str(self.bairro) or \
           str(novo_cliente['cidade'])   != str(self.cidade):

            endereco_completo = novo_cliente['endereco'] + ', ' + novo_cliente['numero'] + ' - ' + novo_cliente['bairro'] + ' - ' + novo_cliente['cidade']
            endereco = parse.quote(endereco_completo)
            api_key ='9V2b8ciJf0K3pqhOB2CahsBkpMYuPJKGHhRabS2-iwY'
            url = 'https://geocode.search.hereapi.com/v1/geocode?q=%s&apiKey=%s'%(endereco,api_key)
            app = MDApp.get_running_app()
            app.popup_leituradados.open()
            req = UrlRequest(url,on_success=self.success, on_error=self.error, on_failure=self.failure)

        else:
            print('Não procurou por novo endereço')

            index = int(self.novo_cliente['codigo']) - 1

            app=MDApp.get_running_app()
            app.patch(self.novo_cliente)

            # Requisitar dados novos
            app.get()
            # Repopular a tela anterior
            app.root.get_screen('Info_tela').adicionar_infos(self)

            # Retirar o popup da tela e voltar para a tela de informações já atualizada
            app = MDApp.get_running_app()
            app.popup_leituradados.dismiss()
            app.root.transition.direction = 'right'
            app.root.current = 'Info_tela'
            app.root.get_screen('Info_tela').adicionar_infos(self)

    def success(self,urlrequest, result):
        print('Success')
        print('tamanho de result:',len(result['items']))
        
        if len(result['items']) == 0:
            app = MDApp.get_running_app()
            app.popup_leituradados.dismiss()
            self.abrir_popup_error()
        else:
            try:
                print(result['items'][0]['access'][0]['lat'])
                print(result['items'][0]['access'][0]['lng'])
                self.novo_cliente['lat'] = result['items'][0]['access'][0]['lat']
                self.novo_cliente['lon'] = result['items'][0]['access'][0]['lng']
            except KeyError:
                app = MDApp.get_running_app()
                app.popup_leituradados.dismiss()
                self.abrir_popup_error()

        # Colocar na base de dados
        app=MDApp.get_running_app()
        app.patch(self.novo_cliente)
        # Requisitar dados novos
        app.get()
        """ # Registrar novo marcador no mapa com novos dados de lat e lon
        #app.root.get_screen('Mapa_tela').verificar_marcadores() """
        # Repopular a tela anterior
        app.root.get_screen('Info_tela').adicionar_infos(self)

        app = MDApp.get_running_app()
        app.popup_leituradados.dismiss()
        app.root.transition.direction = 'right'
        app.root.current = 'Info_tela'
        app.root.get_screen('Info_tela').adicionar_infos(self)

    def error(self,urlrequest, result):
        print('Error')
        app = MDApp.get_running_app()
        app.popup_leituradados.dismiss()
        self.abrir_popup_error()

        # Colocar na base de dados
        app=MDApp.get_running_app()
        app.patch(self.novo_cliente)
        # Requisitar dados novos
        app.get()
        # Repopular a tela anterior
        app.root.get_screen('Info_tela').adicionar_infos(self)
        
        app.root.transition.direction = 'right'
        app.root.current = 'Info_tela'

    def failure(self,urlrequest, result):
        self.error(urlrequest, result)


    def abrir_popup_error(self):
        if not self.popup_error:
            self.popup_error = MDDialog( size_hint = [0.8,0.8],
                title= 'ERRO',
                text = ('As informações foram armazenadas mas houve um erro ao tentar conseguir as coordenadas geográficas para o endereço digitado.' \
                        ' \n'
                        'Não será possivel colocar um marcador para esse cliente no mapa.'),
                buttons=[MDRaisedButton(
                        text="OK", text_color=MDApp.get_running_app().theme_cls.primary_color, on_release = self.fechar
                    ),
                    MDLabel(
                        text='')
                ],
            )
        self.popup_error.open()


    def fechar(self,*args):
        self.popup_error.dismiss()

