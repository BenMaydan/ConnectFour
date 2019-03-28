"""
Main game loop
"""
from classes import Player, ConnectFour


p1 = Player('red', 'schlomo')
p2 = Player('black', 'schlomit')
game = ConnectFour(p1, p2, 6, 7)
somebody_did_not_win = False

while somebody_did_not_win == False:

      game.show_state()
      game.play_turn()
      game.check_win()
