from dbconn import DBFirebase
import os


conn = DBFirebase()
os.system('cls' if os.name == 'nt' else 'clear')
conn.loginFirebase()
os.system('cls' if os.name == 'nt' else 'clear')
print('Bem vindo!')    
opcoes='\n1 - Insere Registro\n2 - Ler Registro\n3 - Alterar Registro\n4 - Apagar Registro\n5 - Apagar Banco de Dados\nDigitar uma opção inválida irá fechar conexão'
while True:
    print(opcoes)
    valor = int(input('\nEscola uma opção: '))
    if valor == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        nome = input('Nome: ')
        cpf = int(input('CPF: '))
        idade = int(input('Idade: '))
        telefone = int(input('Telefone: '))
        cidade = input('Cidade: ')
        uf = input('UF: ')
        conn.insereRegistro(nome,cpf,idade,telefone,cidade,uf)
    elif valor == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        conn.lerRegistro()
    elif valor == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        conn.lerRegistro()
        idRegistro=input('Cole o ID do Resgistro a ser alterado: ')
        nome = input('Nome: ')
        cpf = int(input('CPF: '))
        idade = int(input('Idade: '))
        telefone = int(input('Telefone: '))
        cidade = input('Cidade: ')
        uf = input('UF: ')
        conn.alterarRegistro(nome,cpf,idade,telefone,cidade,uf,idRegistro)
    elif valor == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        conn.lerRegistro()
        idRegistro=input('Cole o ID do Resgistro a ser apagado: ')
        conn.deletarRegistro(idRegistro)
    elif valor == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        certeza = input('Tem certeza? Isso irá deletar toda a tabela (s ou n): ')
        if certeza == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            conn.limparDB()
    else:
        print('Conexão finalizada')
        break
            
