from abbveiculo import *
from tadveiculo import *
class Concessionaria:
    def __init__(self):
        self.quantidadeVeiculos = 0
        self.arvoreVeiculos = ABB()

    #esta função faz a inserção de TADs veiculo em uma árvore de busca binaria
    #além de ir acrescendo a propriedade quantidadeVeiculos a cada vez que se adiciona um novo veiculo
    def inserirVeiculo(self, nome, marca, ano, chassi, preco):
        veiculo = Veiculo(nome=nome,marca=marca,ano=ano, chassi=chassi, preco=preco)
        self.quantidadeVeiculos +=1
        self.arvoreVeiculos.insert(data=veiculo, key=self.retornaChassi(veiculo))

    #neste trecho de código está a função que busca a partir de um Key um veiculo na árvore
    def buscaVeiculo(self, key):
        a = self.arvoreVeiculos.busca(key)
        return a

    #aqui é impresso todos os veiculos dentro da ABB
    def imprimirveiculo(self):
        lista = []
        self.arvoreVeiculos.imprimir(lista)
        for i in lista:
            i.printveiculo()

    #aqui é onde é feita a remoção de veiculos da árvore além de decrescer em uma unidade a propriedade quantidadeVeiculos
    def removerVeiculo(self, chassi):
        self.quantidadeVeiculos -= 1
        self.arvoreVeiculos.remove(chassi)

    #esta função retorna o chassi do veiculo passado como parametro
    def retornaChassi(self, veiculo):
        return veiculo.chassi

    #esta função retorna a quantidade de veiculos cadastrados na concessionaria
    def quantVeiculos(self):
        return (self.quantidadeVeiculos)

    #Aqui é salvo lista de veiculos
    def salvar(self, lista, root=-1):
        if root == -1:
            root = self.arvoreVeiculos.root
        if root is not None:
            self.salvar(lista, root.left)
            lista.append(root.data)
            self.salvar(lista, root.right)
            return lista

    #aqui a lista de veiculos é salva no arquivo veiculo.txt
    def salvaVeiculo_txt(self):
        lista=[]
        lista = self.salvar(lista)
        listaPropriedade = ''
        for i in lista:
            listaPropriedade += i.retornaPropriedade()

        conteudo = listaPropriedade # insira seu conteúdo
        arquivo = open('veiculo.txt', 'w')  # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

        arquivo.close()
        return

    #aqui é carregado todo o cuntéudo do arquivo veiculo.txt  na TAD concessionaria
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
            self.inserirVeiculo(chassi=int(propriedades[i+0]), nome=propriedades[i+1], ano=propriedades[i+2], marca=propriedades[i+3], preco=propriedades[i+4])