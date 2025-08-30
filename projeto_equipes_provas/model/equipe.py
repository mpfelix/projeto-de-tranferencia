class Equipe:
    def __init__(self, nome, membros=None):
        self.nome = nome
        self.membros = membros if membros else []

    def adicionar_membro(self, nome_membro):
        self.membros.append(nome_membro)
