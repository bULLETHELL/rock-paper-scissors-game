import keyboard
import time
class Game:
    def __init__(self, players, BoX):
        self.players = players
        self.BoX = BoX
    
    def StartGame(self):
        turnCounter = 0
        playerOneScoreCounter = 0
        playerTwoScoreCounter = 0
        player1Ready = False
        player2Ready = False
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
        while player1Ready and player2Ready and turnCounter <= self.BoX:
            print('Player One, your weapons are on the following buttons: Rock(a), Paper(s) and Scissors(d)')
            print('Player Two, your weapons are on the following buttons: Rock(j), Paper(k) and Scissors(l)')
            time.sleep(1)
            print('The countdown will begin on the next key press')
            keyboard.read_key()
            print('3')
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            print('GO!')
            

game = Game('dick', 5)
game.StartGame()


