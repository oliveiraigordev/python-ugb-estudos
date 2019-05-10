from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from crud import MyCrud

criar = MyCrud()
criar.criarBD()

with open('test.kv', encoding='utf8') as f: 
    Builder.load_string(f.read())

class Gerenciador(ScreenManager):
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

class Teste(App):
	def build(self):
		return Gerenciador()


Teste().run()