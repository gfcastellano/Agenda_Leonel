
from kivymd.app import MDApp 
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton

class Lembretes_tela(Screen):
    data={'card-plus-outline': 'Adicionar Lembrete'}
    primeiro_dia=''
    primeiro_mes=''
    primeiro_ano=''
    segundo_dia=''
    segundo_mes=''
    segundo_ano=''
    popup_segunda_data=None
    popup_visita=None

    dados_lembretes=[]

    def on_pre_enter(self):
        print('Entrando em Lembretes_tela')
        app = MDApp.get_running_app()
        app.registrar_tela()
        Window.bind(on_keyboard=app.voltar)
        
        self.dados_clientes = app.dados_clientes
        self.dados_visitas  = app.dados_visitas
        if app.telas[-2] == 'Menu_tela':
            self.ids.buscar.text = ''
            self.apagar_lembretes()
        if app.telas[-2] == 'Menu_tela':
            self.ids.scroll.scroll_y=1


    def adicionar_lembretes(self, dados_lembretes):
        print('Adicionando lembretes na tela Lembretes_tela')
        scroll = MDApp.get_running_app().root.get_screen('Lembretes_tela').ids.box_scroll
        if len(dados_lembretes) == 0: #Caso ele receba um match que contem nada
            scroll.add_widget(MDLabel(text='Nenhum resultado encontrado',size_hint_y = None, height = 200, halign = 'center'))      
        for lembrete in reversed(dados_lembretes):
            #print(visita)
            data=lembrete['data']
            scroll.add_widget(Visita(data = data,
                                     nome_fantasia = lembrete['nome_fantasia'],                                     
                                     identificador = str(lembrete['identificador']),
                                     contato = lembrete['contato'],
                                     informacoes = lembrete['informacoes'],
                                     lembrete = lembrete['visita']))

        
    def mostrar_popup(self):
        MDApp.get_running_app().popup_leituradados.open()
        Clock.schedule_once(self.buscar,0.1)

    def buscar(self,*args):
        print('Excutando busca')
        texto = MDApp.get_running_app().root.get_screen('Lembretes_tela').ids.buscar.text
        print('Buscando pelo texto:',texto)
        try:  #Se conseguir transformar em int significa que é pra procurar pelo código
            texto = int(texto)
            texto = str(texto) #se manter no formato int não é possivel iterar
            parametro = 'codigo'
        except ValueError:
            texto = str(texto)
            parametro = 'nome_fantasia'
        self.executar_busca(texto.lower(),parametro)

    def executar_busca(self,texto,parametro):
        print('[executar_busca] texto:',texto)
        print('[executar_busca] parametro:',parametro)
        match=[]
        app = MDApp.get_running_app()

        #################################################
        try:
            self.dados_lembretes = app.dados_lembretes
        except:
            print('Passou')
        #############################################   
        
        for lembrete in self.dados_lembretes:
            if parametro == 'codigo':
                if texto in str(lembrete['codigo']):
                    match.append(lembrete)
            else:
                if texto in str(lembrete['nome_fantasia']).lower():
                    match.append(lembrete)

        remover=[]
        if self.ids.data.text != '':  #Verifica se tem a condição de data
            if len(self.ids.data.text) > 10: #verifica se tem uma ou duas datas
                if self.ordem == 'primeiro':
                    menor_data = self.primeiro_ano + '-' + self.primeiro_mes + '-' + self.primeiro_dia
                    maior_data = self.segundo_ano + '-' + self.segundo_mes + '-' + self.segundo_dia
                else:
                    maior_data = self.primeiro_ano + '-' + self.primeiro_mes + '-' + self.primeiro_dia
                    menor_data = self.segundo_ano + '-' + self.segundo_mes + '-' + self.segundo_dia
                #print(menor_data, maior_data)
                for visita in match:
                    if int(visita['data'][:4]) < int(menor_data[:4]): #verificando ano
                        remover.append(visita)
                    else:
                        if int(visita['data'][:4]) == int(menor_data[:4]) and \
                           int(visita['data'][5:7]) < int(menor_data[5:7]):  #verificando mes
                            if visita in remover:
                                continue
                            else:
                                remover.append(visita)
                        else:
                            if int(visita['data'][:4]) == int(menor_data[:4]) and \
                               int(visita['data'][5:7]) == int(menor_data[5:7]) and \
                               int(visita['data'][8:]) < int(menor_data[8:]): #verificando dia
                                if visita in remover:
                                    continue
                                else:
                                    remover.append(visita)
                    if int(visita['data'][:4]) > int(maior_data[:4]): #verificando ano
                        if visita in remover:
                                continue
                        else:
                            remover.append(visita)
                    else:
                        if int(visita['data'][:4]) == int(maior_data[:4]) and \
                           int(visita['data'][5:7]) > int(maior_data[5:7]): #verificando mes
                            if visita in remover:
                                continue
                            else:
                                remover.append(visita)
                        elif int(visita['data'][:4]) == int(maior_data[:4]) and \
                            int(visita['data'][5:7]) == int(maior_data[5:7]) and \
                            int(visita['data'][8:]) > int(maior_data[8:]):                             
                            if visita in remover:
                                continue
                            else:
                                remover.append(visita)
            else: #significa que só tem uma data na busca
                data = self.primeiro_ano + '-' + self.primeiro_mes + '-' + self.primeiro_dia
                #print(data)
                for visita in self.dados_visitas:
                    if visita['data'] != data:
                        remover.append(visita)       
        
        for lembrete in remover:
            try:
                match.remove(lembrete)
            except ValueError:
                continue
                  
        print('MATCH:',len(match))
        self.apagar_lembretes()
        self.adicionar_lembretes(match)
        self.fechar_popup()
        self.ids.scroll.scroll_y=1

    def apagar_lembretes(self):
        MDApp.get_running_app().root.get_screen('Lembretes_tela').ids.box_scroll.clear_widgets()
        #MDApp.get_running_app().root.get_screen('Info_tela').ids.visitas_tab.ids.box_scroll.clear_widgets()

    def fechar_popup(self):
        MDApp.get_running_app().popup_leituradados.dismiss()

    def apagar_texto(self):
        self.ids.buscar.text = ''
        
    
    def apagar_data(self):
        self.ids.data.text = ''
        #Apagar tambem da vsitas_tab
        

    def abrir_popup_primeira_data(self):
        primeiro_calendario = MDDatePicker(callback = self.abrir_popup_segunda_data)
        primeiro_calendario.open()

    def abrir_popup_segunda_data(self, data):
        self.primeiro_dia = str(data.day) if len(str(data.day)) > 1 else '0'+str(data.day)
        self.primeiro_mes = str(data.month) if len(str(data.month)) > 1 else '0'+str(data.month)
        self.primeiro_ano = str(data.year)
        self.ids.data.text = self.primeiro_dia + '/' + self.primeiro_mes + '/' + self.primeiro_ano
        if not self.popup_segunda_data:
            app = MDApp.get_running_app()
            self.popup_segunda_data = MDDialog( size_hint = [0.8,0.8],
                text='Deseja escolher uma segunda data?\n\nCaso escolha "Sim" será retornado as visitas que estão no intervalo entre as duas datas escolhidas.',
                buttons=[
                    MDRaisedButton(
                        text="Sim", on_release = self.escolher_segunda_data
                    ),
                    MDFlatButton(
                        text="Não", text_color=MDApp.get_running_app().theme_cls.primary_color, on_release = self.fechar_popup_segunda_data
                    )
                ],
            )
        self.popup_segunda_data.open()
    
    def fechar_popup_segunda_data(self,*args):
        self.popup_segunda_data.dismiss()
        MDApp.get_running_app().root.get_screen('Info_tela').ids.visitas_tab.ids.data.text = self.ids.data.text
        if str(MDApp.get_running_app().root.current_screen)[14:-2] == 'Info_tela':
            self.buscar()
    
    def escolher_segunda_data(self,*args):
        self.popup_segunda_data.dismiss()
        segundo_calendario = MDDatePicker(callback = self.segunda_data)
        segundo_calendario.open()

    def segunda_data(self,date, *args):
        #print(data)
        self.segundo_dia = str(date.day) if len(str(date.day)) > 1 else '0'+str(date.day)
        self.segundo_mes = str(date.month) if len(str(date.month)) > 1 else '0'+str(date.month)
        self.segundo_ano = str(date.year)
        
        if int(self.primeiro_ano) == int(self.segundo_ano):
            if int(self.primeiro_mes) == int(self.segundo_mes):
                if int(self.primeiro_dia) == int(self.segundo_dia):
                    pass
                elif int(self.primeiro_dia) < int(self.segundo_dia):
                    self.ids.data.text = self.ids.data.text + ' até ' + self.segundo_dia + '/' + self.segundo_mes + '/' + self.segundo_ano
                    self.ordem = 'primeiro'
                else:
                    self.ids.data.text = self.segundo_dia + '/' + self.segundo_mes + '/' + self.segundo_ano + ' até ' +  self.ids.data.text
                    self.ordem = 'segundo'
            elif int(self.primeiro_mes) < int(self.segundo_mes):
                self.ids.data.text = self.ids.data.text + ' até ' + self.segundo_dia + '/' + self.segundo_mes + '/' + self.segundo_ano
                self.ordem = 'primeiro'
            else:
                self.ids.data.text = self.segundo_dia + '/' + self.segundo_mes + '/' + self.segundo_ano + ' até ' +  self.ids.data.text
                self.ordem = 'segundo'
        elif int(self.primeiro_ano) < int(self.segundo_ano):
            self.ids.data.text = self.ids.data.text + ' até ' + self.segundo_dia + '/' + self.segundo_mes + '/' + self.segundo_ano
            self.ordem = 'primeiro'
        else:
            self.ids.data.text = self.segundo_dia + '/' + self.segundo_mes + '/' + self.segundo_ano + ' até ' +  self.ids.data.text
            self.ordem = 'segundo'
        
        MDApp.get_running_app().root.get_screen('Info_tela').ids.visitas_tab.ids.data.text = self.ids.data.text
        if str(MDApp.get_running_app().root.current_screen)[14:-2] == 'Info_tela':
            self.buscar()

    def ir_para_lembrete_tela(self):
        app = MDApp.get_running_app()
        app.root.get_screen('Lembrete_tela').limpar()
        app.root.get_screen('Lembrete_tela').ids.identificador.text = str(len(self.dados_lembretes))
        app.root.current = 'Lembrete_tela'
        print('Executou')

    def abrir_popup_lembrete(self):    
        if not self.popup_lembrete:
            self.popup_lembrete = MDDialog(
                title="Visita",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL"
                    ),
                    MDFlatButton(
                        text="OK"
                    ),
                ],
            )
        self.popup_lembrete.open()

    
        



class Lembrete(MDCard):
    def __init__(self,data='', nome_fantasia='',contato='',lembrete='', informacoes='',identificador='',**kwargs):
        super().__init__(**kwargs)
        self.ids.data.text          = data
        #self.ids.codigo.text        = codigo
        self.ids.nome_fantasia.text = nome_fantasia
        self.ids.contato.text       = contato
        self.ids.lembrete.text        = lembrete
        self.ids.informacoes.text   = informacoes
        self.ids.identificador.text = identificador

    def abrir_lembrete(self, objeto):
        print('Executando abrir_lembrete')
        app = MDApp.get_running_app()
        app.root.transition.direction = 'left'
        app.root.current = 'Lembrete_tela'
        app.root.get_screen('Lembrete_tela').adicionar_infos(self)


class Content(BoxLayout):
    pass
