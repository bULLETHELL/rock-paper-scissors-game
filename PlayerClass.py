import RockChildClass
import PaperChildClass
import ScissorsChildClass

class Player(object):
    def __init__(self, name, weapons, wins):
        rock = RockChildClass.Rock()
        paper = PaperChildClass.Paper()
        scissors = ScissorsChildClass.Scissors()
        self.name = name
        self.weapons = [rock, paper, scissors]
        self.wins = 0 
    def GetWeaponFromInput(self, input):
        if input == 'a' or 'j':
            return self.weapons[0]
        elif input == 's' or 'k':
            return self.weapons[1]
        elif input == 'd' or 'l':
            return self.weapons[2]
        