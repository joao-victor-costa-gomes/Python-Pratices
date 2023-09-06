import os

def imprimir(pilha):
    for i in range (len(pilha)):
        print(pilha[i])

def adicionar(num, pilha):
    pilha.insert(0, num)

def remover(pilha):
    if (len(pilha)) == 0:
        print("\nSEM ITENS NA PILHA")
    else:    
        pilha.remove(pilha[0])    

pilha = []

while True:
    print("\n1 - Adicionar valor à lista")   
    print("\n2 - Remover valor da lista")   
    print("\n3 - Sair do programa")   
    escolha = eval(input("\nSUA ESCOLHA: "))   

    if escolha == 1:
        num = input("\nDIGITE UM VALOR: ") 
        adicionar(num, pilha)
        print()    
        imprimir(pilha)
        input("\nPressione qualquer tecla...")
        os.system('cls')

    elif escolha == 2:
        print()
        remover(pilha)
        imprimir(pilha)
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

