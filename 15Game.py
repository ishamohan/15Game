#Isha Mohan
#15 Game

from random import randint

class OuterFrame:

    def __init__(self, size):

        self.ht = 0
        self.wid = 0
        self.board_size = size
        self.title_rect = TitleRect(size)
        self.tile_board = TileBoard(size)

    def print_outer_frame(self):
        self.title_rect.print_title_rect()
        self.tile_board.print_board()

    def make_next_move(self):
        a_tile_value = int(raw_input("What number do you want to move? "))
        moving_tile = self.tile_board.get_tile(a_tile_value)
        blank_tile = self.tile_board.get_tile(0)
        if moving_tile.is_adjacent_to(blank_tile):
            self.tile_board.swap_two_tiles(moving_tile, blank_tile)
        else:
            print "Give me another number: "

class TitleRect:

    def __init__(self, board_size):
        self.ht = 0
        self.wid = 0
        self.title = "%d GAME" % int(board_size ** 2 - 1)

    def print_title_rect(self):
        print self.title

class TileBoard:

    def __init__(self, in_size):

        self.ht = 0
        self.wid = 0
        self.size = in_size
        self.tile_array = []
        self.add_tiles()
        #self.set_initial_game_position()

    def add_tiles(self):
        for row in range(0, self.size):
            row_array = []
            for col in range(0, self.size):
                row_array.append(NumTile(-1, row, col))
            self.tile_array.append(row_array)

    def tile_array_has(self, num):
        has_value = False
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.tile_array[row][col].value == num:
                    has_value = True
        return has_value

    def get_tile(self, value):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.tile_array[row][col].value == value:
                    return self.tile_array[row][col]

    def swap_two_tiles(self, tile_1, tile_2):
        temp_tile_1 = NumTile(tile_1.value, tile_1.row, tile_1.col)
        temp_tile_2 = NumTile(tile_2.value, tile_2.row, tile_2.col)
        self.tile_array[tile_1.row][tile_1.col] = temp_tile_2

        self.tile_array[tile_1.row][tile_1.col].row = tile_1.row
        self.tile_array[tile_1.row][tile_1.col].col = tile_1.col

        self.tile_array[tile_2.row][tile_2.col] = temp_tile_1

        self.tile_array[tile_2.row][tile_2.col].row = tile_2.row
        self.tile_array[tile_2.row][tile_2.col].col = tile_2.col

    def move_blank_tile(self):
        blank_tile = self.get_tile(0)
        #print blank_tile.row, blank_tile.col
        random_num = randint(0, 3)
        if random_num == 0:
            if blank_tile.row > 0:
                tile_above = self.tile_array[blank_tile.row - 1][blank_tile.col]
                self.swap_two_tiles(tile_above, blank_tile)
        elif random_num == 1:
            if blank_tile.col < self.size - 1:
                tile_right = self.tile_array[blank_tile.row][blank_tile.col + 1]
                self.swap_two_tiles(tile_right, blank_tile)
        elif random_num == 2:
            if blank_tile.row < self.size - 1:
                tile_down = self.tile_array[blank_tile.row + 1][blank_tile.col]
                self.swap_two_tiles(tile_down, blank_tile)
        else:
            if blank_tile.col > 0:
                tile_left = self.tile_array[blank_tile.row][blank_tile.col - 1]
                self.swap_two_tiles(tile_left, blank_tile)


    def set_random_value(self, row, col):
        rand_num = randint(0, self.size**2 - 1)
        if not (self.tile_array_has(rand_num)):
            self.tile_array[row][col].value = rand_num
            self.tile_array[row][col].row = row
            self.tile_array[row][col].col = col
        else:
            self.set_random_value(row, col)

    def set_one_row(self, row_index):
        num = 0
        col_index = 0
        while col_index < self.size:
            if not self.tile_array_has(num):
                self.tile_array[row_index][col_index].value = num
                col_index += 1
            num += 1

    """def set_initial_game_position(self):
        for row in range(0, self.size - 1):
            for col in range(0, self.size):
                self.set_random_value(row, col)
        self.set_one_row(self.size - 1)"""

    #132-135 sets the amount of random moves computer produced on the board to get the start position

    def set_initial_game_position(self):
        self.set_end_game_position()
        for i in range(0,50):
            self.move_blank_tile()

    def set_end_game_position(self):
        value = 1
        for row in range(0, self.size):
            for col in range(0, self.size):
                self.tile_array[row][col].value = value
                self.tile_array[row][col].row = row
                self.tile_array[row][col].col = col
                value = value + 1
        self.tile_array[self.size - 1][self.size - 1].value = 0

    def is_same_as(self, second_tile_board):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.tile_array[row][col].value != second_tile_board.tile_array[row][col].value:
                    return False
        return True

    def print_board(self):
        print '\n'
        for row in self.tile_array:
            x = " "
            for elem in row:
                if elem.value == 0:
                    x = x + "  " + "_"
                else:
                    x = x + "  " + str(elem.value)
            print x

class NumTile:

    def __init__(self, value, row, col):

        self.value = value
        self.boundary = 0
        self.row = row
        self.col = col

    def is_adjacent_to(self, second_tile):
        if second_tile.row == self.row and (second_tile.col == self.col - 1 or second_tile.col == self.col + 1):
            return True
        elif second_tile.col == self.col and (second_tile.row == self.row - 1 or second_tile.row == self.row + 1):
            return True
        else:
            return False

def main():

    board_size = int(raw_input("Give me a number 'n' that will create a board of size n x n: "))
    board = OuterFrame(board_size)
    board.tile_board.set_initial_game_position()
    board.print_outer_frame()
    end_board =TileBoard(board_size)
    end_board.set_end_game_position()
    #end_board.print_board()
    #second_end_board = TileBoard(board_size)
    #second_end_board.set_end_game_position()
    #second_end_board.print_board()
    #print second_end_board.is_same_as(end_board)

    game_not_over = True

    while game_not_over:
        board.make_next_move()
        board.print_outer_frame()
        if board.tile_board.is_same_as(end_board):
            print "YAY! YOU WIN!"
            game_not_over = False

if __name__ == '__main__':
    main()
