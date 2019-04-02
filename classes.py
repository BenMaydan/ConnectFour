import string
import os
import subprocess
import sys


def clear_terminal():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120


class Chip:

    def __init__(self, color):
        self.color = color


    def __repr__(self):
        return self.color


class Player:

    def __init__(self, color, name):
        self.color = color
        self.name = name


    def play_chip(self):
        return Chip(self.color)


class Display:

    def __init__(self):
        pass


    def draw(self):
        pass


class ConnectFour:
    """
    Column class
    """

    def __init__(self, player_1, player_2, rows, cols):
        self.player_1 = player_1
        self.player_2 = player_2
        self.rows = rows
        self.columns = cols
        self.number_of_turns = 0

        self.ColumFullError = 'Cannot put chip in a full column!'

        self.board = {}
        for i in range(self.columns):
            label = string.ascii_uppercase[i]
            self.board[label] = []


    def play_turn(self):
        if self.number_of_turns % 2 == 0:
            player = self.player_1
        else:
            player = self.player_2

        name = player.name
        try:
            print('\n')
            column = input(str(name[0].upper()) + str(name[1:]) + ', please choose a column: ')
            self.board[column.upper()] = self.board[column.upper()]
            if len(self.board[column.upper()]) == self.rows:
                raise ColumnFullError
        except KeyError:
            print('That is not a valid column!')
        except ColumnFullError:
            print('That column is full!')
            return False
        else:
            self.board[column.upper()].append(player.play_chip())
            self.number_of_turns += 1
            return True


    def show_state(self):
        """
        Shows the state of the board/
        prints board in terminal
        """
        #clear_terminal()
        header = ''
        for key in self.board.keys():
            header += key
        print('-------')
        print(header)
        print('-------')

        #Display column contents
        for i in range(self.rows):
            row_to_show = ''
            for key in self.board.keys():
                if len(self.board[key]) >= self.rows - i:
                    #print(self.board[key], self.rows - i)
                    chip = self.board[key][self.rows - i - 1]
                    row_to_show += chip.color[0] #Shows the first letter of the color / shows 'r' or 'b'
                else:
                    row_to_show += ' '
            print(row_to_show)
        print('-------')


    def check_win(self):
        """
        Checks if there are 4 chips in a row
        (Horizontally/Vertically/Diagonally)
        """
        chips = ''
        if self.number_of_turns % 2 == 0:
            player = self.player_1
        else:
            player = self.player_2
        name = player.name

        #Vertical win check
        for ky in range(len(self.board.keys()), 0, -1):
            index = 0
            key = list(self.board.keys())[index]
            counter = 1
            chip_color = self.board[key][-1].color
            if len(key) >= 4:
                for chip in self.board[key]:
                    if chip.color == chip_color:
                        print('Yes')
                        counter += 1
                        index += 1
                    elif chip_color != chip_color:
                        print('Here')
                        chip_color = chip.color
                        counter = 1
                        index += 1
                    if counter == 4:
                        print(str(name[0].upper()) + str(name[1:]) + ' won!')
                        sys.exit()
                    print(counter)
            else:
                index += 1
            #Do a counter for how many chips in a row
            #1 chip -> counter = 1
            #2 chips same color as prev -> counter = 2
            # Next chip different color -> counter = 1



class ColumnFullError(Exception):
    pass
