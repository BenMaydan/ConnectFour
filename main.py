"""
Main game loop
"""
from classes import Player, ConnectFour, clear_terminal
import sys

p1 = Player('red', 'Schlomo')
p2 = Player('black', 'schlomit')
p3 = Player('yellow', 'Ben')
game = ConnectFour(p1, p2, 6, 7)
somebody_did_not_win = False

while somebody_did_not_win == False:

    try:
        #clear_terminal()
        game.show_state()
        game.play_turn()
        #game.check_win()
    except KeyboardInterrupt:
        print('\nStopping running processes ->')
        sys.exit()
