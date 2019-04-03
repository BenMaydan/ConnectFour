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
        self.listPlayers = []
        self.listPlayers.append(self.player_1)
        self.listPlayers.append(self.player_2)

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
            self.play_turn()
        except IndexError:
            print('That is not a valid column!')
            self.play_turn()
        except ColumnFullError:
           print('That column is full!')
           self.play_turn()
        else:
           self.board[column.upper()].append(player.play_chip())
           self.number_of_turns += 1


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


    def check_win_vertical(self):
        """
        Checks if there are 4 chips in a row
        Vertically
        """
        chips = ''
        if self.number_of_turns % 2 == 0:
            player = self.player_1
        else:
            player = self.player_2
        name = player.name

        #Vertical win check
        for index, ky in enumerate(self.board):
            keyLetter = list(self.board.keys())[index]
            counter = 0
            if len(self.board[keyLetter]) >= 4:
                chip_color = self.board[keyLetter][-1].color
                for chip in self.board[keyLetter]:
                    #If the current chip color is equal to the previous chips color, counter goes up
                    if chip.color == chip_color:
                        counter += 1
                    #If the current chip color is not equal to previous chip color, counter gets reset
                    elif chip.color != chip_color:
                        chip_color = chip.color
                        counter = 1
                    #If there is 4 chips of same color in a row, someone wins
                    if counter == 4:
                        #Determines which player won
                        if chip_color == self.listPlayers[0].color:
                            name = self.listPlayers[0].name
                            print(str(name[0].upper()) + str(name[1:]) + ' won!')
                        else:
                            name = self.listPlayers[1].name
                            print(str(name[0].upper()) + str(name[1:]) + ' won!')
                        sys.exit()
            #Do a counter for how many chips in a row
            #1 chip -> counter = 1
            #2 chips same color as prev -> counter = 2
            # Next chip different color -> counter = 1


    def check_win_horizontal(self):
        """
        Checks if a win occurred
        Horizontally
        """
        list_of_rows = []
        indexOne = 0
        for index, letter in enumerate(self.board):
            row_making = []
            for chip in self.board[letter]:
                try:
                    row_making.append(self.board[letter][indexOne])
                    indexOne += 1
                except:
                    pass
            list_of_rows.append(row_making)
        print(list_of_rows)


        for row in list_of_rows:
            counter = 0
            if len(row) >= 4:
                chip_color = row[-1].color
                for chip in row:
                    #If the current chip color is equal to the previous chips color, counter goes up
                    if chip.color == chip_color:
                        counter += 1
                    #If the current chip color is not equal to previous chip color, counter gets reset
                    elif chip.color != chip_color:
                        chip_color = chip.color
                        counter = 1
                    #If there is 4 chips of same color in a row, someone wins
                    if counter == 4:
                        #Determines which player won
                        if chip_color == self.listPlayers[0].color:
                            name = self.listPlayers[0].name
                            print(str(name[0].upper()) + str(name[1:]) + ' won!')
                        else:
                            name = self.listPlayers[1].name
                            print(str(name[0].upper()) + str(name[1:]) + ' won!')
                        sys.exit()


class ColumnFullError(Exception):
    pass
