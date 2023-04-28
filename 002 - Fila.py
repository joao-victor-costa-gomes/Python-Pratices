import os

def adicionar(fila, item):
    fila.append(item)

def remover(fila):
    if (len(fila)) == 0:
        print("\nSEM ITENS NA FILA")
    else:    
        fila.remove(fila[0])  
      
def imprimir(fila):
    for i in range (len(fila)):
        print(fila[i], end = ' ')

fila = []

while True:
    print("\n1 - Adicionar valor à fila")   
    print("\n2 - Remover valor da fila")   
    print("\n3 - Sair do programa")   
    escolha = eval(input("\nSUA ESCOLHA: "))   

    if escolha == 1:
        item = input("\nDIGITE UM VALOR: ") 
        adicionar(fila, item)
        print()
        imprimir(fila)
        input("\nPressione qualquer tecla...")
        os.system('cls')

    elif escolha == 2:
        remover(fila)
        print()
        imprimir(fila)
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