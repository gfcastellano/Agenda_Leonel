from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker
from datetime import date
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty
from kivy.clock import Clock

import json
from pprint import pprint



class Visita_tela(Screen):
    popup_pesquisa_cliente=None
    popup_pesquisa_contato=None
    popup_pesquisa_visita=None

    def on_pre_enter(self):
        print('Entrando em Visita_tela')
        app = MDApp.get_running_app()
        app.registrar_tela()
        Window.bind(on_keyboard=app.voltar)
        
        self.dados_clientes = app.dados_clientes
        self.dados_visitas  = app.dados_visitas
        #data = date.today()
        #self.primeiro_dia = str(data.day) if len(str(data.day)) > 1 else '0'+str(data.day)
        #self.primeiro_mes = str(data.month) if len(str(data.month)) > 1 else '0'+str(data.month)
        #self.primeiro_ano = str(data.year)
        #self.ids.data.text = self.primeiro_dia + '/' + self.primeiro_mes + '/' + self.primeiro_ano

    def adicionar_infos(self,objeto):
        self.ids.data.text    = objeto.ids.data.text
        #self.ids.codigo.text  = objeto.ids.codigo.text
        self.ids.nome_fantasia.text    = objeto.ids.nome_fantasia.text
        self.ids.contato.text    = objeto.ids.contato.text
        self.ids.informacoes.text    = objeto.ids.informacoes.text
        self.ids.visita.text    = objeto.ids.visita.text
        self.ids.identificador.text    = objeto.ids.identificador.text

    def limpar(self):
        data = date.today()
        self.primeiro_dia = str(data.day) if len(str(data.day)) > 1 else '0'+str(data.day)
        self.primeiro_mes = str(data.month) if len(str(data.month)) > 1 else '0'+str(data.month)
        self.primeiro_ano = str(data.year)
        self.ids.data.text = self.primeiro_dia + '/' + self.primeiro_mes + '/' + self.primeiro_ano
        self.ids.nome_fantasia.text    = ''
        self.ids.contato.text    = ''
        self.ids.informacoes.text    = ''
        self.ids.visita.text    = ''

    def abrir_popup_data(self):
        primeiro_calendario = MDDatePicker(callback = self.marcar_data_visita)
        primeiro_calendario.open()

    def marcar_data_visita(self, data):
        self.primeiro_dia = str(data.day) if len(str(data.day)) > 1 else '0'+str(data.day)
        self.primeiro_mes = str(data.month) if len(str(data.month)) > 1 else '0'+str(data.month)
        self.primeiro_ano = str(data.year)
        self.ids.data.text = self.primeiro_dia + '/' + self.primeiro_mes + '/' + self.primeiro_ano

    def abrir_popup_data_lembrete(self):
        primeiro_calendario = MDDatePicker(callback = self.marcar_data_lembrete)
        primeiro_calendario.open()

    def marcar_data_lembrete(self, data):
        self.primeiro_dia = str(data.day) if len(str(data.day)) > 1 else '0'+str(data.day)
        self.primeiro_mes = str(data.month) if len(str(data.month)) > 1 else '0'+str(data.month)
        self.primeiro_ano = str(data.year)
        self.ids.data_lembrete.text = self.primeiro_dia + '/' + self.primeiro_mes + '/' + self.primeiro_ano

    def mostrar_popup(self):
        MDApp.get_running_app().popup_leituradados.open()
        Clock.schedule_once(self.pesquisar_cliente,0.1)

    def pesquisar_cliente(self,*args):
        MDApp.get_running_app().popup_leituradados.dismiss()
        print('Executando pesquisar_cliente')
        texto = self.ids.nome_fantasia.text
        texto = str(texto).lower()
        match=[]
        for cliente in self.dados_clientes:
            if texto in str(cliente['nome_fantasia']).lower():
                match.append(cliente)
        items=[]
        for cliente in match:
            items.append(Item_cliente(text=cliente['nome_fantasia']))

        #if not self.popup_pesquisa_cliente:
        self.popup_pesquisa_cliente = MDDialog(
            title="Clientes",
            type="simple",
            items=items)
        self.popup_pesquisa_cliente.open()

    def pesquisar_contato(self):
        print('Executando pesquisar_contato')
        texto = self.ids.nome_fantasia.text
        items=[]
        for cliente in self.dados_clientes:
            if texto == cliente['nome_fantasia']:
                dados = cliente
                nome_1, nome_2, nome_3= dados['nome_1'], dados['nome_2'], dados['nome_3']

                
                for nome in [nome_1, nome_2, nome_3]:
                    if len(nome) != 0:
                        items.append(Item_contato(text=nome))
        self.popup_pesquisa_contato = MDDialog(
            title="Contatos cadastrados para esse cliente",
            type="simple",
            items=items)
        self.popup_pesquisa_contato.open()

    def pesquisar_visita(self):
        print('Executando pesquisar_visita')
        items=[Item_visita(text='Presencial'),Item_visita(text='Ligação'),Item_visita(text="Whats"),Item_visita(text="E-mail")]
        
        self.popup_pesquisa_visita = MDDialog(
            title="Tipos de visita",
            type="simple",
            items=items)
        self.popup_pesquisa_visita.open()

    def adicionar_visita(self):
        print("Execuntando adicionar_visita")
        novo_visita={}
        data       = self.ids.data.text
        nome_fantasia   = self.ids.nome_fantasia.text
        contato     = self.ids.contato.text
        visita     = self.ids.visita.text
        informacoes     = self.ids.informacoes.text


        if data == '' or nome_fantasia == '' or contato == '' or visita == '':
            #self.abrir_popup_infos()
            print('Não existem os dados mínimos necessários, não salvando as alterações')
        else:
            print("Existem dados mínimos necessários para adicionar visita")
            novo_visita['data']            = self.ids.data.text
            novo_visita['nome_fantasia']   = self.ids.nome_fantasia.text
            novo_visita['contato']         = self.ids.contato.text
            novo_visita['visita']          = self.ids.visita.text
            novo_visita['informacoes']     = self.ids.informacoes.text
            novo_visita['identificador']   = self.ids.identificador.text
            
            #self.novo_visita = novo_visita

            #self.dados_visitas.append(self.novo_visita)
            #pprint(novo_visita)

        # Colocar dados no Firebase
        app = MDApp.get_running_app()
        app.patch(novo_visita)
        # Requisitar dados novos
        app.get()
        # Repopular a tela anterior
        if app.root.get_screen('Visitas_tela').ids.buscar.text != '':
            app.root.get_screen('Visitas_tela').buscar()
        # Voltar a tela anterior
        app.root.transition.direction = 'right'
        app.root.current = app.telas[-2] # 'Visitas_tela'

    def adicionar_nome_fantasia(self):
        app = MDApp.get_running_app()
        nome_fantasia = app.root.get_screen('Info_tela').ids.info_tab.ids.nome_fantasia.text
        self.ids.nome_fantasia.text = nome_fantasia
        
        data = date.today()
        self.primeiro_dia = str(data.day) if len(str(data.day)) > 1 else '0'+str(data.day)
        self.primeiro_mes = str(data.month) if len(str(data.month)) > 1 else '0'+str(data.month)
        self.primeiro_ano = str(data.year)
        self.ids.data.text = self.primeiro_dia + '/' + self.primeiro_mes + '/' + self.primeiro_ano

    
class Item_cliente(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

    def preencher_cliente(self,text):
        print('Executando preencher_cliente')
        MDApp.get_running_app().root.get_screen('Visita_tela').ids.nome_fantasia.text = text

class Item_contato(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

    def preencher_contato(self,text):
        print('Executando preencher_contato')
        MDApp.get_running_app().root.get_screen('Visita_tela').ids.contato.text = text

class Item_visita(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

    def preencher_visita(self,text):
        print('Executando preencher_visita')
        MDApp.get_running_app().root.get_screen('Visita_tela').ids.visita.text = text

    