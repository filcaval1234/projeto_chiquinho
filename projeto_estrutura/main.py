from tadconscessionaria import *
concessionaria = Concessionaria()
while True:
    condicao = int(input('o que deseja;\n1 --> cadastrar um novo veiculo;\n2 --> buscar veiculo;\n3 --> remover um veiculo; '))
    if condicao is 1:
        nome = input('digite o nome do veiculo: ')
        marca = input('digite a marca do veiculo: ')

        while True:
            try:
                ano = int(input('digite o ano do veiculo: '))
                chassi = int(input('digite o chassi do veiculo: '))
                preco = int(input('digite o preço do veiculo: '))
                break
            except:
                continue
        concessionaria.inserirVeiculo(nome=nome, marca=marca, ano=ano, chassi=chassi, preco=preco)
    elif condicao is 2:
        while True:
            busca = int(input('digite o número do chassi: '))

            if concessionaria.buscaVeiculo(key=busca) is None:
                print("chassi invalido, por favor digite novamente: ")
            else:
                print('----------------------------')
                concessionaria.buscaVeiculo(key=busca).printveiculo()
                break
    elif condicao is 3:
        remove = int(input("digite o chassi do veiculo à ser removido: "))
        concessionaria.removerVeiculo(chassi=remove)

    else:
        print("condição inválida, digite novamente")
        continue