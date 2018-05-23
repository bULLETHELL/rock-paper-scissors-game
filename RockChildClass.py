import WeaponClass

class Rock(WeaponClass.Weapon):
    def __init___(self):
        super.__init__()
    def getName(self):
        return "Rock"
    def getWinsOver(self):
        return "Scissors"
    def getLosesTo(self):
        return "Paper"