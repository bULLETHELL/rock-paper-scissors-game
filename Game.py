import GameClass
import PaperChildClass
import RockChildClass
import ScissorsChildClass
import PlayerClass
players = []
players.append(PlayerClass.Player(input('Player Zero, enter your name\n')))
players.append(PlayerClass.Player(input('Player One, enter your name\n')))

game = GameClass.Game(players, str(input('enter the amount of games in your Best Of series\n')))

game.StartGame()
#STOR PIKsXD