from dbconn import Banco
import os.path
criar=Banco()
#if os.path.exists('base.db') == False:
#	criar.criarTabela()
criar.criarTabela()
opcoes='1 - Insere Registro\n2 - Ler Registro\n3 - Alterar Registro\n4 - Deletar Registro\n5 - Fechar Banco de Dados'
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
		criar.inserirRegistro(i_nome,i_idade,i_cpf,i_fone,i_cidade,i_uf,i_criado_em)
	elif valor == 2:
		parametro=input('Qual paramentro deseja ler? (Deixe vazio para ler todos): ')
		criar.lerRegistro(parametro)
	elif valor == 3:
		i_id = int(input('Qual ID: '))
		i_nome=input('Nome: ')
		i_idade=int(input('Idade: '))
		i_cpf=int(input('CPF: '))
		i_fone=int(input('Telefone: '))
		i_cidade=input('Cidade: ')
		i_uf=input('UF: ')
		i_criado_em=input('Data de cadastro: ')
		criar.alterarRegistro(i_id,i_nome,i_idade,i_cpf,i_fone,i_cidade,i_uf,i_criado_em)
	elif valor == 4:
		del_id = int(input('Qual ID: '))
		criar.deletarRegistro(del_id)
	elif valor == 5:
		criar.fecharConn()
		break
	else:
		print('\nOpção incorreta\n'+opcoes)
