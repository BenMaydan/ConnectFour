"""
Main game loop
"""
from classes import Player, ConnectFour
import sys


p1 = Player('red', 'Schlomo')
p2 = Player('black', 'schlomit')
game = ConnectFour(p1, p2, 6, 7)
somebody_did_not_win = False

while somebody_did_not_win == False:

    try:
        game.show_state(' ')
        game.play_turn()
        game.check_win_vertical()
        game.check_win_horizontal()
    except KeyboardInterrupt:
        print('\nStopping running processes ->')
        sys.exit()
