class MyCrud(object):
    def __init__(self):
        import sqlite3
        self.conexao = sqlite3.connect('base.db')
        self.cursor = self.conexao.cursor()

    def fecharBD(self):
        self.conexao.close()

    def criarBD(self):
        sql = """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR (20) NOT NULL,
                idade INTEGER,
                cpf VARCHAR(11) NOT NULL,
                fone TEXT,
                cidade TEXT,
                uf VARCHAR(2) NOT NULL,
                criado_em DATE NOT NULL
            );
        """
        self.cursor.execute(sql)
        print('Criado com sucesso')

    def lerBD(self, parametro=''):
        if parametro == '':
            sql = """
            select * from clientes;
            """
            self.cursor.execute(sql)
        else:
            sql = """
            select * from clientes where id = ?;
            """
            self.cursor.execute(sql, (parametro,))
        registros = self.cursor.fetchall()
        return registros
        

    def incluirBD(self,p_nome = '',p_idade = '',p_cpf = '',p_fone = '',p_cidade = '',p_uf = '',p_criado_em = ''):
        sql = """
            INSERT INTO clientes (
                id,
                nome,
                idade,
                cpf,
                fone,
                cidade,
                uf,
                criado_em
            )
            VALUES (NULL,?,?,?,?,?,?,?);
        """
        self.cursor.execute(sql, (
            p_nome,
            p_idade,
            p_cpf,
            p_fone,
            p_cidade,
            p_uf,
            p_criado_em            
        ))
        self.conexao.commit()

    def alterarBD(self,a_nome,a_idade,a_cpf,a_fone,a_cidade,a_uf,a_criado_em,a_id):

        sql = """
        update clientes
        set nome = ?,
            idade = ?,
            cpf = ?,
            fone = ?,
            cidade = ?,
            uf = ?,
            criado_em = ?
        where id = ?
        """
        self.cursor.execute(sql, (a_nome,a_idade,a_cpf,a_fone,a_cidade,a_uf,a_criado_em,a_id))
        self.conexao.commit()

    def deletarBD(self,d_id = 0):
        sql = """
        delete from clientes
        where id = ?;
        """
        self.cursor.execute(sql, (d_id,))
        self.conexao.commit()