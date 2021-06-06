### CONSOLE VERSION OF TIC TAC TOE ###
import GameBoard

def main():
    board = GameBoard.GameBoard()
    board.print_board()


    # Create a variable to store the empty game board
    # This should be a column win, print out 'col win' for this one
    gameBoardArray = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
    player = 1
    tieCounter = 0
    isGameover = False

    '''
        Let's write the pseudo code for the program
        
        display the empty gameboard before loop starts
        
        This will loop 'infinitely':
            - getChoice
            - placePiece
            - display gameboard
            - checkWin
            - checkTie
            - If win, display win -- Reset
            - If tie, display tie -- Reset
            - else, switchPlayer. Continue loop
    '''
    printGameBoard(gameBoardArray)

    while not isGameover:
        choice = getChoice(gameBoardArray)

        gameBoardArray = placePiece(player, choice, gameBoardArray)
        tieCounter = incTieCounter(tieCounter)

        printGameBoard(gameBoardArray)

        win = checkWin(gameBoardArray, player)
        tie = checkTie(tieCounter, win)

        if win:
            print("Player " + str(player) + " WINS!")
            playAgain = askPlayAgain()
            if not playAgain: isGameover = True
            else:
                gameBoardArray = [[' ', ' ', ' '],
                                  [' ', ' ', ' '],
                                  [' ', ' ', ' ']]
                player = 1
                tieCounter = 0

        elif tie:
            print("Tie Game!")
            playAgain = askPlayAgain()
            if not playAgain: isGameover = True
            else:
                gameBoardArray = [[' ', ' ', ' '],
                                  [' ', ' ', ' '],
                                  [' ', ' ', ' ']]
                player = 1
                tieCounter = 0

        else:
            player = switchPlayer(player)



def getChoice(gameBoardArray):
    inputChoice = False

    while not inputChoice:
        row = int(input("Enter a row [1-3]: "))
        col = int(input("Enter a column [1-3]: "))

        # Check if the choice is a valid move
        if gameBoardArray[row-1][col-1] == ' ' and 0 < row <= 3 and 0 < col <= 3:
            return row - 1, col - 1

def askPlayAgain():
    choice = input("Would you like to play again?[y/n]: ")
    if choice == 'y' or choice == 'Y':
        return True
    return False

def placePiece(player, choice, gameBoardArray):
    piece = 'x' if player == 1 else 'o'
    row = choice[0]
    col = choice[1]

    gameBoardArray[row][col] = piece
    return gameBoardArray

def checkWin(gameBoardArray, player):
    piece = 'x' if player == 1 else 'o'
    winCheck = False

    # Check the rows first
    for row in range(3):
        for col in range(3):
            if gameBoardArray[row][col] == piece:
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
            if(gameBoardArray[row][col] == piece):
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
        if gameBoardArray[i][i] == piece:
            winCheck = True
        else:
            winCheck = False
            break
    if winCheck:
        print("Diag Win")
        return winCheck

    # Check for Anti Diagonal Win
    for i in range(3):
        if gameBoardArray[2-i][i] == piece:
            winCheck = True
        else:
            winCheck = False
            break
    if winCheck:
        print("Anti Diag Win")
        return winCheck

    # If it's gotten to this statement, no win was found. This will always return FALSE
    return winCheck

def checkTie(tieCounter, win):
    if tieCounter >= 9 and not win:
        return True
    return False

def switchPlayer(player):
    if player == 1:
        return 2
    else:
        return 1

def incTieCounter(tieCounter):
    return tieCounter + 1

def resetTieCounter(tieCounter):
    return 0

def printGameBoard(gameBoardArray):
    """
        This will print the current state of the
        game board from the array
        Should look something similar to this:

           | o | x
        -----------
           |   |
        -----------
           |   |

        This won't be used in the GUI version of this
        but is needed for the console version.
    """

    # Take the number of element + 2 (3 rows for pieces, 2 for borders)
    for x in range(3):
        for y in range(3):
            print(" " + gameBoardArray[x][y] + " ", end="")
            if y < 2: print("|", end="")
        print()
        if x < 2: print("-----------")


if __name__ == "__main__":
    main()
