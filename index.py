print(' ')
produto = input("Qual e o produto que vai a ser adicionado: ")
print(' ')
categoria = input("qual a categoria de seu produto: ")
print(' ')
qtd = input('Quantas unidades o produto possui: ')
print(' ')


if produto and categoria and qtd:
    qtd = int(qtd)
    if categoria == "bebidas":
        if qtd < 75:
            print(' ')
            print('Favor solicitar mais bebidas stock com', qtd, 'unidades disponivel')
        elif qtd > 75:
            print(' ')
            print("Stock cheio!")
        elif qtd == 75:
            print(' ')
            print("Stock de bebidas está igual o valor minimo que e de 75")

    if categoria == "limpeza":
            if qtd < 35:
                print(' ')
                print("Favor solicitar mais", categoria, "stock com", qtd, "unidades")
            elif qtd > 35:
                 print(' ')
                 print("Stock cheio!")
            elif qtd == 35:
                print(' ')
                print("Stock de limpeza está igual o valor minimo que e de 35")
else:
    print(" ")
    print("Por gentileza preencha as informações sugeridas acima.")
