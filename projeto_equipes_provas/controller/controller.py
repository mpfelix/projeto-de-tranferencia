from model.equipe import Equipe
from model.banco import Banco

class Controller:
    def __init__(self):
        self.banco = Banco()
        self.banco.criar_tabelas()
        self.equipes = []

    def cadastrar_equipe(self, nome, membros):
        equipe = Equipe(nome, membros)
        self.equipes.append(equipe)

        self.banco.cursor.execute("INSERT INTO equipes (nome) VALUES (%s)", (nome,))
        equipe_id = self.banco.cursor.lastrowid
        for m in membros:
            self.banco.cursor.execute("INSERT INTO membros (nome, equipe_id) VALUES (%s, %s)", (m, equipe_id))
        self.banco.conn.commit()
