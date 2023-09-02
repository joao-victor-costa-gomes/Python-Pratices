import status
from status import Pokemon
import os

pokemon = Pokemon()
name = input("DIGITE O NOME DO SEU POKEMON: ")

pokemon.nome(name)
pokemon.status()

while True:

    print('''\nO QUE DESEJA FAZER?
            
    1 - BATALHAR
    2 - VER STATUS DO POKEMON
    3 - CURAR POKEMON
    4 - SAIR
    ''')
    escolha = eval(input("SUA ESCOLHA: "))

    if escolha == 1:
            pokemon.batalha()
            input("\nPressione qualquer tecla...")
            os.system('cls')

    elif escolha == 2:
        pokemon.mostrar_status()
        input("\nPressione qualquer tecla...")
        os.system('cls')

    elif escolha == 3:
        pokemon.cura()
        input("\nPressione qualquer tecla...")
        os.system('cls')

    elif escolha == 4:
        print("\nFIM DO PROGRAMA")
        input()
        break

    else: 
        print("\nESCOLHA INVÁLIDA")
        input("\nPressione qualquer tecla...")
        os.system('cls')
            
      
    


