from itertools import permutations
import numpy as np
import json

saveboard = []


def check_win(board: np.array, player: int):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_draw(board: np.array):
    return (
        not np.any(board == -1) and not check_win(board, 0) and not check_win(board, 1)
    )


def unique_permutations(elements):
    unique_perms = set()
    for perm in permutations(elements):
        unique_perms.add(tuple(perm))
    return unique_perms


elements = [0, 0, 0, 0, 0, 1, 1, 1, 1]
perms = unique_permutations(elements)

for perm in perms:
    board = np.array(perm).reshape(3, 3)
    if check_win(board, 1):
        print("Player Min wins!")
        saveboard.append([board.tolist(), -10])
    elif check_win(board, 0):
        print("Player Max wins!")
        saveboard.append([board.tolist(), 10])
    elif check_draw(board):
        print("Draw!")
        saveboard.append([board.tolist(), 0])

with open("game_data.json", "w") as f:
    json.dump(saveboard, f)
