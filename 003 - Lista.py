import os

def adicionar(lista, item):
    lista.append(item)

def remover(lista, item):
    if item not in lista:
        print("\nNão exite esse item na lista")
    else:
        lista.remove(item)

def imprimir(lista):
    for i in range (len(lista)):
        print(lista[i], end = '\n')

lista = ['maça', 'banana', 'uva']

while True:
    print("\nLISTA DE COMPRAS")
    print("\n1 - Adicionar produto à lista")   
    print("\n2 - Remover produto da lista")   
    print("\n3 - Sair do programa")   
    escolha = eval(input("\nSUA ESCOLHA: "))   

    if escolha == 1:
        item = input("\nDIGITE O NOME DO PRODUTO: ") 
        adicionar(lista, item)
        print()
        imprimir(lista)
        input("\nPressione qualquer tecla...")
        os.system('cls')

    elif escolha == 2:
        print()
        imprimir(lista)
        removido = input("\nQUAL ITEM VOCÊ QUER REMOVER? ")
        remover(lista, removido)
        print()
        imprimir(lista)
        input("\nPressione qualquer tecla...")
        os.system('cls')

    elif escolha == 3:
        print("\nFIM DO PROGRAMA")
        input()
        break

    else: 
        print("\nESCOLHA INVÁLIDA")
        input("\nPressione qualquer tecla...")
        os.system('cls')