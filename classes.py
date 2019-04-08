import string
import sys
import numpy as np
import random


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


class ConnectFour:
    """
    Column class
    """

    def __init__(self, player_1, player_2, rows, cols):
        random_first_player = {1:True, 2:False}
        player_2_goes_first = random_first_player[random.randrange(1, 3)]
        medium_to_switch_players = None
        if player_2_goes_first == True:
            medium_to_switch_players = player_1
            player_1 = player_2
            player_2 = medium_to_switch_players
        self.player_1 = player_1
        self.player_2 = player_2
        self.rows = rows
        self.columns = cols
        self.number_of_turns = 0
        self.listPlayers = [player_1, player_2]
        self.ColumFullError = 'Cannot put chip in a full column!'

        #The line below all the way to line number 72 is error checking
        #For the correct type and length of both the row and the column
        self.RowLengthError = RowLengthError()
        self.ColumnLengthError = ColumnLengthError()
        self.RowTypeError = RowTypeError()
        self.ColumnTypeError = ColumnTypeError()
        self.RowLengthErrorMSG = 'Invalid Row Length. Try a Number Greater Than 0!'
        self.ColumnLengthErrorMSG = 'Invalid Column Length. Try a Number Greater Than 0!'
        self.RowTypeErrorMSG = 'Invalid type for "row" parameter. Use an integer!'
        self.ColumnTypeErrorMSG = 'Invalid type for "column" parameter. Use an integer!'
        try:
            if type(self.rows) != int:
                raise RowTypeError
            if type(self.columns) != int:
                raise ColumnTypeError
            if self.rows <= 0:
                raise RowLengthError
            if self.columns <= 0:
                raise ColumnLengthError
        except RowLengthError:
            print(self.RowLengthErrorMSG)
            sys.exit()
        except ColumnLengthError:
            print(self.ColumnLengthErrorMSG)
            sys.exit()
        except RowTypeError:
            print(self.RowTypeErrorMSG)
            sys.exit()
        except ColumnTypeError:
            print(self.ColumnTypeErrorMSG)
            sys.exit()
        else:
            pass


        self.board = {}
        self.letters_to_index = {}
        index = 0
        #Generates correct number of columns
        for i in range(self.columns):
            label = string.ascii_uppercase[i]
            self.board[label] = []
            self.letters_to_index[label] = index
            index += 1

        self.board_list = [[]]
        #Generates all of the rows in one list
        #I.E. a 2d/2 dimensional list
        for x in range(self.rows):
            self.board_list.append([])
        #Puts correct number on None's in rows
        for row in self.board_list:
            for y in range(self.columns):
                self.board_list[y].append(None)


    def play_turn(self):
        if self.number_of_turns % 2 == 0:
            player = self.player_1
        else:
            player = self.player_2

        #Uses substringing to capitalize first letter of name +
        #Also capitalizes first letter of player color
        player_name = str(player.name[0].upper() + str(player.name[1:]))
        player_color = str(player.color[0].upper() + player.color[1:])

        #Error checking for the correct input and to make sure
        #That the chip that was chosen can go in a correct column/row
        try:
            print('\n\n')
            column = input(player_name + '/' + player_color + ', please choose a column: ')
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
            chip = player.play_chip()
            if len(self.board[column.upper()]) == 0:
                row_number = self.rows
            else:
                row_number = self.rows - len(self.board[column.upper()])
            #print("Insert into list at index:", self.letters_to_index[column.upper()])
            self.board_list[row_number].pop(self.letters_to_index[column.upper()])
            self.board_list[row_number].insert(self.letters_to_index[column.upper()], chip)
            #for x in self.board_list:
            #    print(x)

            self.board[column.upper()].append(chip)
            self.number_of_turns += 1


    def show_state(self, spacingBetweenLetters):
        """
        Shows the state of the board/
        prints board in terminal
        """

        header = ''
        for key in self.board.keys():
            header += key + spacingBetweenLetters

        numDashes = len(header)
        dashes = ''
        for n in range(numDashes):
            dashes += '-'

        #Actually prints dashes and header
        #Header is the letters A - G
        print(dashes)
        print(header)
        print(dashes)

        #Display column contents
        for i in range(self.rows):
            row_to_show = ''
            for key in self.board.keys():
                if len(self.board[key]) >= self.rows - i:
                    #Defines what a chip is and adds it the the row to show which it will print later
                    chip = self.board[key][self.rows - i - 1]
                    row_to_show += chip.color[0] + spacingBetweenLetters#Shows the first letter of the color / shows 'r' or 'b' and some amount of spaces after
                else:
                    row_to_show += '-' + spacingBetweenLetters
            print(row_to_show)
        print(dashes)


    def check_win_vertical(self, spacingBetweenLetters):
        """
        Checks if there are 4 chips in a row
        Vertically
        """
        chips = ''

        #Determines which player turn it is
        if self.number_of_turns % 2 == 0:
            player = self.player_1
        else:
            player = self.player_2
        name = player.name

        #Vertical win check
        for index, ky in enumerate(self.board):
            keyLetter = list(self.board.keys())[index]
            counter = 0
            #If the len of the column is less than 4, it won't bother
            #Even checking if there are 4 colors in a row
            if len(self.board[keyLetter]) >= 4:
                chip_color = self.board[keyLetter][-1].color
                for chip in self.board[keyLetter]:
                    if chip == None:
                        pass
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
                            print("\nThe winning state of the board:")
                            self.show_state(spacingBetweenLetters)
                        else:
                            name = self.listPlayers[1].name
                            print(str(name[0].upper()) + str(name[1:]) + ' won!')
                            print("\nThe winning state of the board:")
                            self.show_state(spacingBetweenLetters)
                        sys.exit()
            #Do a counter for how many chips in a row
            #1 chip -> counter = 1
            #2 chips same color as prev -> counter = 2
            # Next chip different color -> counter = 1


    def check_win_horizontal(self, spacingBetweenLetters):
        """
        Checks if a win occurred horizontally
        """
        person_that_won = self.loop_and_use_counter(self.board_list)
        if person_that_won == None:
            pass
        else:
            print(str(person_that_won[0].upper()) + str(person_that_won[1:]) + ' won!')
            print("\nThe winning state of the board:")
            self.show_state(spacingBetweenLetters)
            sys.exit()


    def check_win_diagonally(self, spacingBetweenLetters):
        """
        This check win method starts at the top left chip and goes to the right, with every diagonal it checks
        having a positive slope

        [ = start
        ] = end
        c = chip

        [c] c] c] c]
        [c  c  c  c]
        [c  c  c  c]
        [c [c [c [c]
        """
        #import main
        array = np.array(self.board_list)

        #This vertically mirrors the original array so the wanted diagonals are
        # lower-right-to-upper-left.
        diagonals = [array[::-1,:].diagonal(i) for i in range(-array.shape[0]+1,array.shape[1])]

        # Opposite of the line above
        diagonals.extend(array.diagonal(i) for i in range(array.shape[1]-1,-array.shape[0],-1))

        #Converts back to Python lists from numpy arrays
        for n in diagonals:
            n = n.tolist()

        #Loops over and uses a counter to check if there are 4 in a row
        #After it calls the method, if it returns a name, it prints the player that won
        #Else, it doesn't do anything and lets the two players return to playing the game
        person_that_won = self.loop_and_use_counter(diagonals)
        if person_that_won == None:
            pass
        else:
            print(str(person_that_won[0].upper()) + str(person_that_won[1:]) + ' won!')
            print("\nThe winning state of the board:")
            self.show_state(spacingBetweenLetters)
            sys.exit()


    def loop_and_use_counter(self, two_dimensional_list):
        """
        Loops over and uses a counter to check if there are 4 in a row
        """
        for row in two_dimensional_list:
            counter = 0
            #If the len of the row is less than 4, it won't bother
            #Even checking if there are 4 colors in a row
            if len(row) >= 4:
                if row[-1] == None:
                    chip_color = None
                    counter = 0
                else:
                    chip_color = row[-1].color
                for chip in row:
                    #Moves on to next iteration if there is no chip
                    if chip == None:
                        counter = 0
                        continue
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
                            return name
                        else:
                            name = self.listPlayers[1].name
                            return name


    def check_if_tie(self, spacingBetweenLetters):
        """
        Checks if the whole board was filled up and no one won
        """
        counter = 0
        for column in self.board:
            if len(column) == self.columns:
                counter += 1
            if len(column) != self.columns:
                break
            if counter == len(rows):
                #The computer likes to be fair,
                #So it chose a random number including 1 and 2
                #And used that to determine which player is printed first
                #In the tie msg string
                random_player_in_string = {1:True, 2:False}
                player_1_goes_first_in_str = random_first_player[random.randrange(1, 3)]
                player_1_name = self.player_1.name[0].upper() + self.player_1.name[1:]
                player_2_name = self.player_2.name[0].upper() + self.player_2.name[1:]
                if player_1_goes_first_in_str == True:
                    msg = "Neither " + str(player_1_name) + " nor " + str(player_2_name) + " won."
                else:
                    msg = "Neither " + str(player_2_name) + " nor " + str(player_1_name) + " won."

                #Prints the tie message
                print(msg)
                print("The game ended in a tie...")
                print("\nThe last state of the board:")
                self.show_state(spacingBetweenLetters)
                sys.exit()


#Errors I can raise for incorrect/broken input from player
class ColumnFullError(Exception):
    pass
class RowLengthError(Exception):
    pass
class RowTypeError(Exception):
    pass
class ColumnLengthError(Exception):
    pass
class ColumnTypeError(Exception):
    pass
