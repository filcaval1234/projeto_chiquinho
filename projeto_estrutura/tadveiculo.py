class Veiculo:
    def __init__(self, nome, marca, ano, chassi, preco):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.chassi = chassi
        self.preco = preco

    def printveiculo(self):
        print('nome=', self.nome)
        print('marca=', self.marca)
        print('ano=', self.ano)
        print('chassi=', self.chassi)
        print('preço=',self.preco)
        print('----------------------------')

    def retornaPropriedade(self):
        return str('\n'+'-------------------------------'+'\n''Chassi do carro: '+str(self.chassi)+'\n'+'Nome do carro: '+self.nome+'\n'+
                   'Ano: '+ str(self.ano)+'\n''Marca: '+self.marca+'\n'+ 'Preço: '+str(self.preco))



