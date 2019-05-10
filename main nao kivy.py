from dbconn import Banco
import os.path
db=Banco()
#if os.path.exists('base.db') == False:
#	criar.criarTabela()
db.criarTabela()
opcoes='\n1 - Insere Registro\n2 - Ler Registro\n3 - Alterar Registro\n4 - Apagar Registro\n5 - Fechar Banco de Dados'
print(opcoes)
while True:

	valor = int(input('\nDigite a opção: '))
	if valor == 1:
		i_nome=input('Nome: ')
		i_idade=int(input('Idade: '))
		i_cpf=int(input('CPF: '))
		i_fone=int(input('Telefone: '))
		i_cidade=input('Cidade: ')
		i_uf=input('UF: ')
		i_criado_em=input('Data de cadastro: ')
		db.inserirRegistro(i_nome,i_idade,i_cpf,i_fone,i_cidade,i_uf,i_criado_em)
		print(opcoes)
	elif valor == 2:
		registroid=input('Qual registro deseja ler? (Digite o ID ou deixe em branco para listar todos - 0 para voltar): ')
		if registroid == 0:
			pass
			print(opcoes)
		else:
			db.lerRegistro(registroid)
			print(opcoes)
	elif valor == 3:
		a_id=int(input('Digite o ID do registro a ser alterado - 0 para voltar: )'))
		if a_id == 0:
			pass
			print(opcoes)
		else:
			a_nome=input('Nome: ')
			a_idade=int(input('Idade: '))
			a_cpf=int(input('CPF: '))
			a_fone=int(input('Telefone: '))
			a_cidade=input('Cidade: ')
			a_uf=input('UF: ')
			a_criado_em=input('Data de cadastro: ')
			db.alterarRegistro(a_id,a_nome,a_idade,a_cpf,a_fone,a_cidade,a_uf,a_criado_em)
			print(opcoes)
	elif valor == 4:
		del_id = int(input('Qual registro deseja apagar? (Digite o ID - 0 para voltar): '))
		if del_id == 0:
			pass
			print(opcoes)
		db.deletarRegistro(del_id)
		print(opcoes)
	elif valor == 5:
		db.fecharConn()
		break
	else:
		print('\nOpção incorreta\n'+opcoes)
