import random
import os

class Pokemon:

    def nome(self, name):
        self.Pokenome = name

    def status (self):

        self.exp = 0

        self.nivel = 1

        self.HPMAX = 45

        self.HP = 45
        self.Attack = 50 
        self.Defense = 50
        self.Sp_Attack = 65
        self.Sp_Defense = 65
        self.Speed = 45

    def mostrar_status (self):
        print('''\nSTATUS DO {0}
        
        NÍVEL: {1}
        - HP = {2}
        - Attack = {3} 
        - Defense = {4}
        - Sp_Attack = {5}
        - Sp_Defense = {6}
        - Speed = {7}'''.format(self.Pokenome, self.nivel, self.HP , self.Attack, self.Defense, self.Sp_Attack, self.Sp_Defense, self.Speed))

    def evoluir (self):
        self.nivel = self.nivel + 1

        self.HPMAX = self.HPMAX + int(self.HPMAX * 0.2) 

        self.HP = self.HP + int(self.HP * 0.2)
        self.Attack = self.Attack + int(self.Attack * 0.2)
        self.Defense = self.Defense + int(self.Defense * 0.2)
        self.Sp_Attack = self.Sp_Attack + int(self.Sp_Attack * 0.2)
        self.Sp_Defense = self.Sp_Defense + int(self.Sp_Defense * 0.2)
        self.Speed = self.Speed + int(self.Speed * 0.2)

    def cura (self):
        if self.HP >= self.HPMAX:
            print("\nO SEU POKÉMON ESTÁ COM A VIDA CHEIA!\n")
        else:
            self.HP = self.HPMAX
            print("\nSEU POKEMON FOI CURADO\n")

    def experiencia (self):
        self.exp =  self.exp + 300
        if self.exp%900 == 0:
            print("\nGANHOU +1 NÍVEL!\n")  
            self.evoluir()
            print("\nPARABÉNS SEU POKEMON EVOLUIU!\n")
            self.mostrar_status()
        else:
            pass 

    def batalha (self):
        if self.HP == 0:
            print("TEU POKEMON TÁ ABATIDO MEU IRMÃO!\n")
        else:
            self.HP = self.HP - random.randint(1, self.HP)
            if self.HP == 0:
                print("\nSeu pokémon perdeu a batalha...\n")
            else:
                print("\nSeu pokémon venceu a batalha!") 
                self.experiencia()  

