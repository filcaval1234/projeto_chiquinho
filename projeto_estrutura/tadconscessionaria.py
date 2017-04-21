from abbveiculo import *
from tadveiculo import *

class Concessionaria:
    def __init__(self):
        self.quantidadeVeiculos = 0
        self.arvoreVeiculos = ABB()

    def inserirVeiculo(self, nome, marca, ano, chassi, preco):
        veiculo = Veiculo(nome=nome,marca=marca,ano=ano, chassi=chassi, preco=preco)
        self.quantidadeVeiculos +=1
        self.arvoreVeiculos.insert(data=veiculo, key=self.retornaChassi(veiculo))

    def buscaVeiculo(self, key):
        a = self.arvoreVeiculos.busca(key)
        return a

    def imprimirveiculo(self):
        lista = []
        self.arvoreVeiculos.imprimir(lista)
        for i in lista:
            i.printveiculo()

    def removerVeiculo(self, chassi):
        self.quantidadeVeiculos -= 1
        self.arvoreVeiculos.remove(chassi)

    def retornaChassi(self, veiculo):
        return veiculo.chassi
