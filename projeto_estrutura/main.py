from tadconscessionaria import *
concessionaria = Concessionaria()
concessionaria.voltaPraArvore()
while True:
    condicao = int(input('o que deseja;\n1 --> cadastrar um novo veiculo;\n2 --> buscar veiculo;\n3 --> remover um veiculo;\n4 --> quantidade de veiculos no estoque;\n5 --> sair;\n6 --> salvar;\n '))
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

    elif condicao is 4:
        print('A quantidade de carros é',concessionaria.quantVeiculos())

    elif condicao is 5: break

    elif condicao is 6: concessionaria.salvaVeiculo_txt()

    else:
        print("condição inválida, digite novamente")
        continue