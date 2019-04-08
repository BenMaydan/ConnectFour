"""
Main game loop
"""
from classes import Player, ConnectFour
import sys
import numpy as np


p1 = Player('red', 'Dan')
p2 = Player('black', 'Ben')
game = ConnectFour(p1, p2, 6, 7)
spacingBetweenLetters = '  '


somebody_did_not_win = False
while somebody_did_not_win == False:

    try:
        game.show_state(spacingBetweenLetters)
        game.play_turn()
        game.check_win_vertical()
        game.check_win_horizontal()
        game.check_win_diagonally()
    except KeyboardInterrupt:
        print('\nStopping running processes ->')
        sys.exit()
