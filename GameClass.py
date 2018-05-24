import keyboard
import PlayerClass
import time
class Game:
    def __init__(self, players, BoX):
        self.players = players
        self.BoX = int(BoX)
        self.player0 = players[0]
        self.player1 = players[1]
    
    def StartGame(self):
        turnCounter = 0
        player1Ready = False
        player2Ready = False
        print('%s, Press "s" to be ready \n%s, Press "k" to be ready' % (self.player0.name, self.player1.name))
        while True:#making a loop
            try: #used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('s') and keyboard.is_pressed('k'):#
                    print('you are ready')
                    player1Ready = True
                    player2Ready = True
                    break#finishing the loop
                else:
                    pass
            except:
                break
        while player1Ready and player2Ready and turnCounter < self.BoX:
            print('%s, your weapons are on the following buttons: Rock(a), Paper(s) and Scissors(d)' % self.player0.name)
            print('%s, your weapons are on the following buttons: Rock(j), Paper(k) and Scissors(l)' % self.player1.name)
            time.sleep(1)
            print('The countdown will begin on the next key press, make sure to make your choice by the end')
            keyboard.read_key()
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('GO!')
            inputlist = keyboard.stash_state()
            print(inputlist)
            input1 = ''
            input2 = ''
            for i in inputlist:
                if i == 30: input1 = 'a'
                elif i == 31: input1 = 's'
                elif i == 32: input1 = 'd'

                if i == 36: input2 = 'j'
                elif i == 37: input2 = 'k'
                elif i == 38: input2 = 'l'
            ##################determine weapon for this round#################
            
            self.player0.GetWeaponFromInput(input1)
            self.player1.GetWeaponFromInput(input2)
            print(self.player0.equippedWeapon.getName(), self.player1.equippedWeapon.getName())
            
            ################determine winner of this round###################
            if self.player0.equippedWeapon.getWinsOver() == self.player1.equippedWeapon.getName():
                self.player0.wins += 1
                turnCounter += 1
                print('%s Wins this round' % self.player0.name)
            elif self.player0.equippedWeapon.getLosesTo() == self.player1.equippedWeapon.getName():
                self.player1.wins += 1
                turnCounter += 1
                print('%s wins this round' % self.player1.name)
            elif self.player0.equippedWeapon.getName() == self.player1.equippedWeapon.getName():
                print('This round was ends in a draw, neither %s or %s wins this round' % (self.player0.name, self.player1.name))
            time.sleep(2)
            input('press enter to continue\n')
        if self.player0.wins > self.player1.wins:
            print('congratulations %s you are the winner of this Bo%s' % (self.player0.name, self.BoX))
        elif self.player0.wins < self.player1.wins:
            print('congratulations %s you are the winner of this Bo%s' % (self.player1.name, self.BoX))
        elif self.player0.wins == self.player1.wins:
            print('this Bo%s ends in a draw, no winners' % self.BoX)
        input('press enter to quit')
            
