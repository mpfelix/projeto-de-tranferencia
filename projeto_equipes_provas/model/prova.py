from abc import ABC, abstractmethod

class Prova(ABC):
    def __init__(self, nome, pontuacao_max):
        self.nome = nome
        self.pontuacao_max = pontuacao_max

    @abstractmethod
    def calcular_pontuacao(self, *args):
        pass


class ProvaTeorica(Prova):
    def __init__(self, nome, pontuacao_max, num_questoes):
        super().__init__(nome, pontuacao_max)
        self.num_questoes = num_questoes

    def calcular_pontuacao(self, acertos):
        return (acertos / self.num_questoes) * self.pontuacao_max


class ProvaPratica(Prova):
    def __init__(self, nome, pontuacao_max, tempo_limite):
        super().__init__(nome, pontuacao_max)
        self.tempo_limite = tempo_limite

    def calcular_pontuacao(self, tempo_gasto):
        return max(0, self.pontuacao_max - (tempo_gasto - self.tempo_limite))
