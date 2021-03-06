"""  A module to create a two player tic tac toe game.
view => model => controller

- initialize game board ()
- player 1 : X
- player 2 : O

postions:
1 2 3
4 5 6
7 8 9

how the game will look in the terminal

_ _ _      X _ _     X _ O    X _ O
_ _ _  =>  _ _ _  => _ _ _ => _ X _
_ _ _      _ _ _     _ _ _    _ _ _

"""
import sys


def tic_tac_toe():
    """Main Game function. Contains game loop."""
    gameState = initialize()
    gameOver = False
    res = 0
    xTurn = True
    while not gameOver:
        print_state(gameState, xTurn)
        pos = int(input('enter next position: '))
        while not valid_pos(gameState, pos):
            print('invalid position. Please try again')
            pos = int(input('enter next position: '))
        gameState = newState(gameState, pos, xTurn)
        xTurn = not xTurn
        gameOver, res = check_gameOver(gameState)

    # print result
    print('Tic Tac Toe')
    print('-----------')
    print()
    print("positions labeled from 1 to 9")
    print("1  2  3")
    print("4  5  6")
    print("7  8  9")
    print()
    print('current game board:')
    for row in gameState:
        print(*list(map(converter, row)))
    print()
    # print winner
    print(winner(res))
    # restart?
    restart = input('type r to restart & any other key to exit: \n\n\n')
    if restart == "r" or restart == "R":
        tic_tac_toe()
    sys.exit()


def initialize():
    """Initializes the gameBoard by returning a 3*3 array of 0s."""
    board = []
    for _ in range(3):
        board.append([0]*3)
    return board


def print_state(board, xTurn):
    """Prints the instructions and current state of the board."""
    # 0 => _
    # 1 => X
    # 2 => O

    print('Tic Tac Toe')
    print('-----------')
    print()
    print("positions labeled from 1 to 9")
    print("1  2  3")
    print("4  5  6")
    print("7  8  9")
    print()
    print('current game board:')
    for row in board:
        print(*list(map(converter, row)))
    print()
    if xTurn:
        print("X's Turn")
    else:
        print("O's Turn")


def converter(elem):
    """While printing the board, converts 0s, 1s and 2s to respective ASCII characters."""
    if elem == 0:
        return "_"
    elif elem == 1:
        return "X"
    else:
        return "O"


def valid_pos(board, pos):
    """Checks if the position entered by user is valid (in range and empty)."""
    res = False
    if pos < 1 or pos > 9:
        return False
    elif pos == 1 and board[0][0] == 0:
        res = True
    elif pos == 2 and board[0][1] == 0:
        res = True
    elif pos == 3 and board[0][2] == 0:
        res = True
    elif pos == 4 and board[1][0] == 0:
        res = True
    elif pos == 5 and board[1][1] == 0:
        res = True
    elif pos == 6 and board[1][2] == 0:
        res = True
    elif pos == 7 and board[2][0] == 0:
        res = True
    elif pos == 8 and board[2][1] == 0:
        res = True
    elif pos == 9 and board[2][2] == 0:
        res = True
    return res


def newState(board, pos, xTurn):
    """Takes the old state of the game and the new position, and based on whose turn it is (X or O), it updates the gameState and returns it."""
    if xTurn:
        value = 1
    else:
        value = 2
    if pos == 1:
        board[0][0] = value
    if pos == 2:
        board[0][1] = value
    if pos == 3:
        board[0][2] = value
    if pos == 4:
        board[1][0] = value
    if pos == 5:
        board[1][1] = value
    if pos == 6:
        board[1][2] = value
    if pos == 7:
        board[2][0] = value
    if pos == 8:
        board[2][1] = value
    if pos == 9:
        board[2][2] = value
    return board


def check_gameOver(board):
    """Checks if the game is over. Considers all gameover conditions as listed below."""
    # top row
    if board[0][0] == board[0][1] == board[0][2] != 0:
        return True, board[0][0]
    # middle row
    elif board[1][0] == board[1][1] == board[1][2] != 0:
        return True, board[1][0]
    # bottom row
    elif board[2][0] == board[2][1] == board[2][2] != 0:
        return True, board[2][0]
    # left column
    elif board[0][0] == board[1][0] == board[2][0] != 0:
        return True, board[0][0]
    # middle column
    elif board[0][1] == board[1][1] == board[2][1] != 0:
        return True, board[0][1]
    # right column
    elif board[0][2] == board[1][2] == board[2][2] != 0:
        return True, board[0][2]
    # top-left diagonal
    elif board[0][0] == board[1][1] == board[2][2] != 0:
        return True, board[0][0]
    # top-right diagonal
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return True, board[0][2]
    # no empty space
    elif tie(board):
        return True, -1
    else:
        return False, None


def tie(board):
    """Checks if the game has tied. If board has no 0s, then game is tied"""
    for row in board:
        if 0 in row:
            return False
    return True


def winner(res):
    """Returns result of the game after the game is over"""
    if res == 1:
        return "X is the winner!\n"
    elif res == 2:
        return "O is the winner!\n"
    else:
        return "the game is tied!\n"

# to test
# b1 = [[2, 0, 1],
#       [0, 1, 2],
#       [1, 0, 1]]


# initial game call
if __name__ == "__main__":
    tic_tac_toe()
