from flask_mysqldb import MySQLdb

class PessoaDao:
    def __init__(self):
        self.__conexao = MySQLdb.connect(
                        host="mysql.topskills.study" 
                        ,database="topskills01"
                        ,user="topskills01"
                        ,passwd="ts2019"
                        )
        self.__cursor = self.__conexao.cursor()

    def listar_todos(self):
        self.__cursor.execute("SELECT * FROM 01_PN_PESSOA")
        for p in self.__cursor.fetchall():
            print(f'id:{p[0]} nome:{p[1]} sobrenome:{p[2]} idade:{p[3]} sexo:{p[4]}')

    def buscar_por_id(self, id):
        self.__cursor.execute(F"SELECT * FROM 01_PN_PESSOA WHERE ID = {id}")
        p = self.__cursor.fetchone()
        print(f'id:{p[0]} nome:{p[1]} sobrenome:{p[2]} idade:{p[3]} sexo:{p[4]}')

    def inserir(self, nome, sobrenome, idade, sexo):
        self.__cursor.execute(f"""
                                INSERT INTO 01_PN_PESSOA
                                (
                                    NOME
                                    ,SOBRENOME
                                    ,IDADE
                                    ,SEXO
                                )
                                VALUES
                                (
                                    '{nome}'
                                    ,'{sobrenome}'
                                    ,{idade}
                                    ,'{sexo}'
                                )
                                """)
        self.__conexao.commit()

    def alterar(self, id, nome, sobrenome, idade, sexo):
         self.__cursor.execute(f"""
                                UPDATE 01_PN_PESSOA
                                SET 
                                    NOME = '{nome}'
                                    ,SOBRENOME = '{sobrenome}'
                                    ,IDADE = {idade}
                                    ,SEXO = '{sexo}'
                                WHERE ID = {id}
                                """)
         self.__conexao.commit()

    def deletar(self, id):
        self.__cursor.execute(f"""
                                DELETE FROM 01_PN_PESSOA
                                WHERE ID = {id}
                                """)
        self.__conexao.commit()