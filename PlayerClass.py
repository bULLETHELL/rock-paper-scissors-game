import RockChildClass
import PaperChildClass
import ScissorsChildClass
import WeaponClass

class Player(object):
    def __init__(self, name):
        rock = RockChildClass.Rock()
        paper = PaperChildClass.Paper()
        scissors = ScissorsChildClass.Scissors()
        self.name = name
        self.weapons = [rock, paper, scissors]
        self.wins = 0 
        self.equippedWeapon = self.weapons[0]
    def GetWeaponFromInput(self, input):
        if input == 'a' or input == 'j':
            self.equippedWeapon = self.weapons[0]
        elif input == 's' or input == 'k':
            self.equippedWeapon = self.weapons[1]
        elif input == 'd' or input == 'l':
            self.equippedWeapon = self.weapons[2]
    def GetEquippedWeaop(self):
        return self.equippedWeapon
        