from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.lang import Builder
from dbconn import DBFirebase

criar = DBFirebase()


with open('test.kv', encoding='utf8') as f:
    Builder.load_string(f.read())

class Gerenciador(ScreenManager):
    pass

class Login(Screen):
    def entrar(self):
        usuario = self.ids.iptUser.text
        senha = self.ids.iptPass.text
        if criar.loginFirebase(usuario,senha):
            App.get_running_app().root.current = 'g_menu'
        self.ids.iptUser.text = ''
        self.ids.iptPass.text = ''

class Menu(Screen):
    def fecharApp(self):
        App.get_running_app().stop()

class Clientes(Screen):
    def addCliente(self):
        pNome = self.ids.iptNome.text
        print(pNome)
        pCPF = self.ids.iptCPF.text
        print(pCPF)
        pIdade = self.ids.iptIdade.text
        print(pIdade)
        pTelefone = self.ids.iptTelefone.text
        print(pTelefone)
        pCidade = self.ids.iptCidade.text
        print(pCidade)
        pUF = self.ids.iptUF.text
        print(pUF)
        criar.insereRegistro(pNome,pCPF,pIdade,pTelefone,pCidade,pUF)
        self.ids.iptNome.text = ''
        self.ids.iptIdade.text = ''
        self.ids.iptCPF.text = ''
        self.ids.iptTelefone.text = ''
        self.ids.iptCidade.text = ''
        self.ids.iptUF.text = ''

class Pesquisar(Screen):
    def addWidget(self):
        chave_pesquisar = self.ids.iptPesquisar.text
        self.registros = criar.lerRegistro(chave_pesquisar)
        for i in self.registros:
            print(i.key(),i.val())
            self.ids.box.add_widget(Tarefa(
                 textid=i.key(),
                 textnome=i.val().get('nome'),
                 textcpf=i.val().get('cpf'),
                 textidade=i.val().get('idade'),
                 texttelefone=i.val().get('telefone'),
                 textcidade=i.val().get('cidade'),
                 textuf=i.val().get('uf')))

        self.ids.iptPesquisar.text = ''


class Tarefa(BoxLayout):
    def __init__(self, textid='', textnome='', textcpf='',textidade='', texttelefone='', textcidade='', textuf='', **kwargs):
        super().__init__(**kwargs)
        self.ids.labelid.text = textid
        self.ids.labelnome.text = textnome
        self.ids.labelcpf.text = textcpf
        self.ids.labelidade.text = textidade
        self.ids.labeltelefone.text = texttelefone
        self.ids.labelcidade.text = textcidade
        self.ids.labeluf.text = textuf

    def delCliente(self):
        print(self.ids.labelid.text)
        criar.deletarRegistro(self.ids.labelid.text)

class UpdateClientes(Screen):
    def __init__ (self, tarefas=[], **kwargs):
        super().__init__(**kwargs)

    def telaCliente(self, idCliente=''):

        resultado = criar.lerRegistro(idCliente)
        self.idCliente = idCliente
        for i in resultado:
            self.ids.iptNome.text = i.val().get('nome')
            self.ids.iptCPF.text = i.val().get('cpf')
            self.ids.iptIdade.text = i.val().get('idade')
            self.ids.iptTelefone.text = i.val().get('telefone')
            self.ids.iptCidade.text = i.val().get('cidade')
            self.ids.iptUF.text = i.val().get('uf')


    def updateCliente(self):
        criar.alterarRegistro(self.ids.iptNome.text,self.ids.iptCPF.text,self.ids.iptIdade.text,self.ids.iptTelefone.text,self.ids.iptCidade.text,self.ids.iptUF.text,self.idCliente)


class Teste(App):
    def build(self):
        return Gerenciador()


Teste().run()