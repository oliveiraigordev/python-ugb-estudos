import pyrebase
import getpass

class DBFirebase:
    def __init__ (self):
        self.config = {
        "apiKey": "ALTERAR",
        "authDomain": "ALTERAR,
        "databaseURL": "ALTERAR",
        "storageBucket": "ALTERAR"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        
    def loginFirebase(self):
        self.auth = self.firebase.auth()
        self.username = input('Email: ')
        self.passw = getpass.getpass('Senha:')
        try:
            self.user = self.auth.sign_in_with_email_and_password(self.username,self.passw)
            self.db = self.firebase.database() 
        except:
            print('Usuário ou senha incorretos')
            self.loginFirebase()
           
    
    def insereRegistro(self,iptNome,iptCpf=0,iptIdade=0,iptTelefone=0,iptCidade='',iptUf=''):
        dados = {
            "nome":iptNome,
            "cpf":iptCpf,
            "idade":iptIdade,
            "telefone":iptTelefone,
            "cidade":iptCidade,
            "uf":iptUf
            }
        self.db.child("clientes").push(dados)
        #self.db.child("clientes").push(dados, self.user['idToken'])
        #self.db.child("clientes").child(iptNome+str(iptCpf)).set(dados, self.user['idToken'])
    def lerRegistro(self):
        self.userselect = self.db.child("clientes").get()
        for usuario in self.userselect.each():
            print(usuario.key())
            print(usuario.val())
            print('-'*60)
    def alterarRegistro(self,altNome,altCpf=0,altIdade=0,altTelefone=0,altCidade='',altUf='',altId=''):
        dados = {
            "nome":altNome,
            "cpf":altCpf,
            "idade":altIdade,
            "telefone":altTelefone,
            "cidade":altCidade,
            "uf":altUf
            }
        self.db.child("clientes").child(altId).update(dados)
    def deletarRegistro(self,delId):
        self.db.child("clientes").child(delId).remove()
    def limparDB(self):
        confirma = getpass.getpass('Digite sua senha:')
        if confirma == self.passw:
            self.db.child("clientes").child().remove()
        else:
            print('Senha incorreta')