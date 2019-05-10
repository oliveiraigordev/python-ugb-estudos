class Banco():
	def __init__ (self):
		import sqlite3
		self.conn = sqlite3.connect('base.db')
		self.cursor = self.conn.cursor()

	def criarTabela(self):
		sql= """
		CREATE TABLE IF NOT EXISTS clientes(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			nome VARCHAR(20) NOT NULL,
			idade INTEGER,
			cpf VARCHAR(11) NOT NULL,
			fone TEXT,
			cidade TEXT,
			uf VARCHAR(2) NOT NULL,
			criado_em DATE NOT NULL
			);
			"""
		self.cursor.execute(sql)
		print ('Criado com sucesso!')

	def inserirRegistro(self,i_nome,i_idade,i_cpf,i_fone,i_cidade,i_uf,i_criado_em):
		sql="""
		INSERT INTO clientes (nome,idade,cpf,fone,cidade,uf,criado_em)
	    VALUES (?,?,?,?,?,?,?)
	    """
		self.cursor.execute(sql, (i_nome,i_idade,i_cpf,i_fone,i_cidade,i_uf,i_criado_em))
		self.conn.commit()
		return 'Registro inserido com sucesso!'

	def lerRegistro(self, parametro=''):
		if parametro=='':
			sql="""
			SELECT * FROM clientes;
			"""
			self.cursor.execute(sql)
		else:
			sql="""
			SELECT * FROM clientes WHERE id = ?;
			"""
			self.cursor.execute(sql, parametro)
		registros = self.cursor.fetchall()

		for linha in registros:
		    print(linha)

	def alterarRegistro(self,i_id,i_nome,i_idade,i_cpf,i_fone,i_cidade,i_uf,i_criado_em):
		sql="""
		UPDATE clientes
		SET nome = ?,
		idade = ?,
		cpf = ?,	
		fone = ?,
		cidade = ?,
		uf = ?,
		criado_em = ?
		WHERE id = ?
		"""
		self.cursor.execute(sql,(i_nome,i_idade,i_cpf,i_fone,i_cidade,i_uf,i_criado_em,i_id))
		self.conn.commit()

	def deletarRegistro(self,del_id):
		sql="""
		DELETE FROM clientes
		WHERE id = ?
		"""
		self.cursor.execute(sql, (del_id,))
		self.conn.commit()

	def fecharConn(self):
		self.conn.close()
		print ('Conexão com DB finalizada!')

