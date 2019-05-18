import pyrebase

class DBFirebase:
    def __init__ (self):
        self.config = {
        "apiKey": "PEGUE OS DADOS NO FIREBASE",
        "authDomain": "PEGUE OS DADOS NO FIREBASE",
        "databaseURL": "PEGUE OS DADOS NO FIREBASE",
        "storageBucket": "PEGUE OS DADOS NO FIREBASE"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        
    def loginFirebase(self):
        self.auth = self.firebase.auth()
        username = input('Digite seu email: ')
        passw = input('Digite sua senha: ')
        try:
            self.user = self.auth.sign_in_with_email_and_password(username,passw)
            self.db = self.firebase.database() 
            print('Conectado')
        except:
            print('Usuário ou senha incorretos')
            self.loginFirebase()
           
    
    def criarTabela(self,iptNome,iptCpf=0,iptIdade=0,iptTelefone=0,iptCidade='',iptUf=''):
        clientes = {
            "nome":iptNome,
            "cpf":iptCpf,
            "idade":iptIdade,
            "telefone":iptTelefone,
            "cidade":iptCidade,
            "uf":iptUf
            }
        