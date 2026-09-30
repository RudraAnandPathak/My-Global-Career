"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # First we count the number of X's and O's
    X_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    # For the initial state
    if X_count == 0 and o_count == 0:
        return X
    # For the upcoming moves
    elif X_count > o_count:
        return O
    elif o_count >= X_count:
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # We create a set to store actions
    actions = set()
    # We check each cell
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))  # Add the cells if found empty to the set and then return it
    return actions

            
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception
    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]
    # Check columns
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]

    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # If the game is already over, there is no move to make.
    if terminal(board):
        return None

    def value(board):
        """
        Returns the utility value of a board assuming
        both players play optimally.
        """

        # If the game is over, return its utility:
        # X win = 1, tie = 0, O win = -1
        if terminal(board):
            return utility(board)

        # X wants to maximize the value.
        if player(board) == X:
            best_value = -math.inf

            # Consider every possible move for X.
            for action in actions(board):
                new_board = result(board, action)
                new_value = value(new_board)

                # Keep the highest value found.
                if new_value > best_value:
                    best_value = new_value

        # O wants to minimize the value.
        else:
            best_value = math.inf

            # Consider every possible move for O.
            for action in actions(board):
                new_board = result(board, action)
                new_value = value(new_board)

                # Keep the lowest value found.
                if new_value < best_value:
                    best_value = new_value

        return best_value

    # Now choose the actual move that gives the current player
    # the best possible value.
    if player(board) == X:
        best_value = -math.inf
        best_action = None

        for action in actions(board):
            new_board = result(board, action)
            new_value = value(new_board)

            if new_value > best_value:
                best_value = new_value
                best_action = action

    else:
        best_value = math.inf
        best_action = None

        for action in actions(board):
            new_board = result(board, action)
            new_value = value(new_board)

            if new_value < best_value:
                best_value = new_value
                best_action = action

    return best_action
