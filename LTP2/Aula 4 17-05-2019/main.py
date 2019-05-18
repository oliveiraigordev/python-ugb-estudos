from dbconn import DBFirebase


'''
opcoes='\n1 - Insere Registro\n2 - Ler Registro\n3 - Alterar Registro\n4 - Apagar Registro\n5 - Fechar Banco de Dados'
print(opcoes)
while True:
'''

conn = DBFirebase()
conn.loginFirebase()

#conn.criarTabela()
