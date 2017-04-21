from abbveiculo import *
from tadveiculo import *

class Concessionaria:
    def __init__(self):
        self.quantidadeVeiculos = 0
        self.arvoreVeiculos = ABB()

    def inserirVeiculo(self, nome, marca, ano, chassi, preco):
        veiculo = Veiculo(nome=nome,marca=marca,ano=ano, chassi=chassi, preco=preco)
        self.quantidadeVeiculos +=1
        self.arvoreVeiculos.insert(veiculo, self.retornaChassi(veiculo))

    def retornaChassi(self, veiculo):
        return veiculo.chassi
