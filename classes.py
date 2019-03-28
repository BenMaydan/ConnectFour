
import string

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
        print(name[0].upper() + name[1:] + "'s turn.'")
        try:
            column = input('Please choose a column: ')
        except KeyError:
            print('NOT A VALID KEY!')

        if len(self.board[column]) == self.rows:
            print('Column', column, 'is full')
            return False

        else:
            self.board[column].append(player.play_chip())
            self.number_of_turns += 1
            print(self.board)
            return True


    def show_state(self):
        print(self.board)


    def check_win(self):
        pass
