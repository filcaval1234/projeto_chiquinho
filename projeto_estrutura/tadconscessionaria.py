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

    def quantVeiculos(self):
        return (self.quantidadeVeiculos)

    def salvar(self, lista, root=-1):
        if root == -1:
            root = self.arvoreVeiculos.root
        if root is not None:
            self.salvar(lista, root.left)
            lista.append(root.data)
            self.salvar(lista, root.right)
            return lista

    def salvaVeiculo_txt(self):
        lista=[]
        lista = self.salvar(lista)
        listaPropriedade = ''
        for i in lista:
            listaPropriedade += i.retornaPropriedade()

        #arquivo = open('veiculo.txt', 'r').read()  # Abra o arquivo (leitura)
        conteudo = listaPropriedade # insira seu conteúdo

        arquivo = open('veiculo.txt', 'w')  # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

        arquivo.close()
        return

    def voltaPraArvore(self):
        arquivo = open('veiculo.txt').read()
        arquivo = arquivo.split("\n")
        listaArquivo = []
        propriedades = []
        for i in range(len(arquivo)):
            listaArquivo.append(arquivo[i].split(": "))
        for i in range(len(listaArquivo)):
            if len(listaArquivo[i]) is 2:
                propriedades.append(listaArquivo[i][1])
        for i in range(0, len(propriedades), 5):
            a=int(propriedades[i+0])
            print(type(a))
            self.inserirVeiculo(chassi=int(propriedades[i+0]), nome=propriedades[i+1], ano=propriedades[i+2], marca=propriedades[i+3], preco=propriedades[i+4])
