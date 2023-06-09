class Retângulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura 
    
    def __repr__(self):
        return f'Retângulo {self.altura}x{self.largura}'

class Círculo:
    def __init__(self, raio, perímetro):
        self.raio = raio 
        self.perímetro = perímetro

    def __repr__(self):
        return f'Círculo de raio {self.raio}'

class Shape:
    def calcularArea(forma):
        if isinstance(forma, Retângulo) == True:
            area = forma.altura * forma.largura
            return area 
        
        if isinstance(forma, Círculo) == True:
            area = pow(forma.raio, 2) * 3.14
            return area 
        
class item_Fila:
    def __init__(self, item):
         self.item = item 
         self.área = Shape.calcularArea(item)
         self.prox = None

    def __repr__(self):
         return f'{self.item}'

class Fila:
    def __init__(self):
        self.fila = []
        self.lista_área = []
        self.início = None

    def add(self, forma):

        novo_nó = item_Fila(forma)

        if self.início is None:
            self.início = novo_nó
   
        else:
            atual = self.início
            while atual.prox:
                atual = atual.prox
            atual.prox = novo_nó

        self.fila.append(novo_nó)
 
    def imprimir(self):
        for forma in self.fila:
            print(f'{forma.item} --> {forma.prox}')

    def listar_áreas(self):
       for item in self.fila:
           self.lista_área.append(item.área)

    def imprimir_áreas(self):
        for área in self.lista_área:
            print(área)

    def calcularArea(self):
        self.listar_áreas()
        total = sum(self.lista_área)
        print(f'Valor total das áreas: {total}')
        #print("")
        #self.imprimir_áreas()

print("")

#Retângulos
r1 = Retângulo(2, 4)
r2 = Retângulo(3, 6)
r3 = Retângulo(4, 8)

#Círculos
c1 = Círculo(2, 2)
c2 = Círculo(3, 2)
c3 = Círculo(4, 2)

bloco = Fila()
bloco.add(r1)
bloco.add(c1)
bloco.add(r2)
bloco.add(c2)
bloco.add(r3)
bloco.add(c3)
bloco.imprimir()
print("")
bloco.calcularArea()

input("\nFim do programa...")

