import WeaponClass

class Scissors(WeaponClass.Weapon):
    def __init___(self):
        super.__init__()
    def getName(self):
        return "Scissors"
    def getWinsOver(self):
        return "Paper"
    def getLosesTo(self):
        return "Rock"

