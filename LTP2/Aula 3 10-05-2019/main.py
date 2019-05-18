from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.lang import Builder
from crud import MyCrud

criar = MyCrud()
criar.criarBD()
criar.criarLogin()

with open('test.kv', encoding='utf8') as f: 
    Builder.load_string(f.read())

class Gerenciador(ScreenManager):
	pass

class Login(Screen):
	def login(self):
		usuario = self.root.ids.iptUser.text
		senha = self.root.ids.iptPass.text
		if usuario == 'admin' and senha == 'admin':
			pass

class Menu(Screen):
	def fecharBanco(self):
		criar.fecharBD()
		print('Banco fechado!!!')
		App.get_running_app().stop()

class Clientes(Screen):
	def addCliente(self):
		pNome = self.ids.iptNome.text
		print(pNome)
		pIdade = self.ids.iptIdade.text
		print(pIdade)
		pCPF = self.ids.iptCPF.text
		print(pCPF)
		pTelefone = self.ids.iptTelefone.text
		print(pTelefone)
		pCidade = self.ids.iptCidade.text
		print(pCidade)
		pUF = self.ids.iptUF.text
		print(pUF)
		pData = self.ids.iptData.text
		print(pData)
		criar.incluirBD(pNome,pIdade,pCPF,pTelefone,pCidade,pUF,pData)
		self.ids.iptNome.text = ''
		self.ids.iptIdade.text = ''
		self.ids.iptCPF.text = ''
		self.ids.iptTelefone.text = ''
		self.ids.iptCidade.text = ''
		self.ids.iptUF.text = ''
		self.ids.iptData.text = ''

class Pesquisar(Screen):
	def addWidget(self):
		pesquisar = self.ids.iptPesquisar.text
		registros = criar.lerBD(pesquisar)
		print (registros)
		for i in registros:
		 	self.ids.box.add_widget(Tarefa(
		 		textid=str(i[0]),
		 		textnome=i[1],
		 		textcpf=str(i[3]),
		 		textidade=str(i[2]),
		 		texttelefone=str(i[4]),
		 		textcidade=str(i[5]),
		 		textuf=i[6]))
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
		criar.deletarBD(self.ids.labelid.text)

class UpdateClientes(Screen):
	def __init__ (self, tarefas=[], **kwargs):
		super().__init__(**kwargs)

	def telaCliente(self, idCliente=0):

		self.cliente_id = idCliente
		resultado = criar.lerBD(self.cliente_id)[0]
		print(self.cliente_id)
		print(resultado)
		self.ids.iptNome.text = resultado[1]
		self.ids.iptIdade.text = str(resultado[2])
		self.ids.iptCPF.text = str(resultado[3])
		self.ids.iptTelefone.text = str(resultado[4])
		self.ids.iptCidade.text = resultado[5]
		self.ids.iptUF.text = resultado[6]
		self.ids.iptData.text = resultado[7]

	def updateCliente(self):
		criar.alterarBD(self.ids.iptNome.text,self.ids.iptIdade.text,self.ids.iptCPF.text,self.ids.iptTelefone.text,self.ids.iptCidade.text,self.ids.iptUF.text,self.ids.iptData.text,self.cliente_id)



class Teste(App):
	def build(self):
		return Gerenciador()


Teste().run()