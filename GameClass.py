import keyboard
class Game:
    def __init__(self, players, BoX):
        self.players = players
        self.BoX = BoX
    
    def StartGame(self):
         player1Ready = False
         player2Ready = False
         while True:#making a loop
            print('dickhead')
            try: #used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('s') and keyboard.is_pressed('k'):#if key 'q' is pressed 
                    print('you are ready')
                    break#finishing the loop
                else:
                    pass
            except:
                break #if user pressed a key other than the given key the loop will break

game = Game('dick', 5)
game.StartGame()


