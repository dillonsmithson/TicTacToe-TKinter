""" GameBoard Class
    This class will hold the game board to be used for the game
    For now, the game board is hard coded as a 3x3 matrix, but this
    can be changed so that the game board can be dynamic. Maybe in the
    future.
"""


class GameBoard:
    """ Initialize a new board for the game. It will initialize as empty."""

    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    """ Print out the current state of the game board. """

    def print_board(self):
        for x in range(3):
            for y in range(3):
                print(" " + self.board[x][y] + " ", end="")
                if y < 2:
                    print("|", end="")
            print()
            if x < 2:
                print("-----------")

    """ Returns True or False based on the validity of the move 
        A move is valid if the space is empty and is within the 
        confines of the boards x and y size. 
    """

    def _check_move(self, position):
        if 0 < position[0] <= 2 and 0 < position[1] <= 2:
            if self.board[position[0]][position[1]] == ' ':
                return True

    """ Updates the board with a move the player makes only if that move is
        valid. Will make a call to _check_move for that logic. Keeps asking the 
        use for input, until the input is valid
    """

    def get_move_and_place(self):
        inputChoice = False

        while not inputChoice:
            row = int(input("Enter a row [1-3]: "))-1
            col = int(input("Enter a col [1-3]: "))-1

            # Check move
            position = (row, col)
            inputChoice = self._check_move(position)
            if not inputChoice:
                print("Choice invalid... Try Again,")

    """ Will return true if the player that's passed makes a winning move. 
        This seems a lot longer than what it needs to be, and honestly I could
        probably clean up some of the logic, but this logic is made so that I 
        don't have to change too much when coming back to make the game board
        dynamic. This code is pretty much setup to be dynamic. Although, I may
        need to cap the row/col limit to 10, since the row and col checks are 
        O(n^2). 
    """

    def win_check(self, player):
        winCheck = False
        piece = player.get_type()

        # Check the rows first
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == piece:
                    winCheck = True
                else:
                    winCheck = False
                    break
            if winCheck:
                # Use something here if I wanna check if its a row win
                print("Row Win")
                return winCheck

        # Now check for Column win
        for col in range(3):
            for row in range(3):
                if self.board[row][col] == piece:
                    winCheck = True
                else:
                    winCheck = False
                    break
            if winCheck:
                # Use something here if I wanna check if its a column win
                print("Col Win")
                return winCheck

        # Check for Diagonal win
        for i in range(3):
            if self.board[i][i] == piece:
                winCheck = True
            else:
                winCheck = False
                break
        if winCheck:
            print("Diag Win")
            return winCheck

        # Check for Anti Diagonal Win
        for i in range(3):
            if self.board[2 - i][i] == piece:
                winCheck = True
            else:
                winCheck = False
                break
        if winCheck:
            print("Anti Diag Win")
            return winCheck

        # If it's gotten to this statement, no win was found. This will always return FALSE
        return winCheck
