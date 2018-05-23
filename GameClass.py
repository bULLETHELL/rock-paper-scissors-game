class Game:
    def __init__(self, players, BoX):
        self.players = players
        self.BoX = BoX
    
    def StartGame(self):
         player1Ready = False
         player2Ready = False
         while not player1Ready and player2Ready:
             print("Players, press one your second button to indicate ready (for Player 1; 'S', for Player 2: 'K'")
             if raw_input(':')[0].char
        