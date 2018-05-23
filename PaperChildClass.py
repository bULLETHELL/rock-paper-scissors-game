import WeaponClass

class Paper(WeaponClass.Weapon):
    def __init___(self):
        super.__init__()
    def getName(self):
        return "Paper"
    def getWinsOver(self):
        return "Rock"
    def getLosesTo(self):
        return "Scissors"