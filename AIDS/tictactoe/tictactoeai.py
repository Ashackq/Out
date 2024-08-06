import random
from itertools import permutations
import json

with open('game_data.json', 'r') as f:
    loaded_saveboard = json.load(f)

# dynamic
WIN = 10
LOSS = -10
DRAW = 0

init_state = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
PRINT_WINS = "Player Wins"
PRINT_LOSSES = "Player Losses"

import math

def evaluate(state):
  # Simple evaluation function:
  # Check for wins, losses, or draws
  # Return a score based on the outcome
  # For a more complex game, this evaluation function would be crucial
  # ...
  pass

def minimax(state, depth, is_maximizing):
  if depth == 0 or end(state):
    return evaluate(state)

  if is_maximizing:
    max_eval = -math.inf
    for move in get_possible_moves(state):
      new_state = make_move(state, move, 1)  # Assuming 1 is the maximizing player
      eval = minimax(new_state, depth - 1, False)
      max_eval = max(max_eval, eval)
    return max_eval
  else:
    min_eval = math.inf
    for move in get_possible_moves(state):
      new_state = make_move(state, move, 0)
      eval = minimax(new_state, depth - 1, True)
      min_eval = min(min_eval, eval)
    return min_eval

def get_possible_moves(state):
  # Return a list of empty cell coordinates
  pass

def make_move(state, move, player):
  # Create a new state with the move applied
  pass

def miner_ply(state):
  # Use minimax to find the best move for the minimizing player
  best_move = None
  best_value = math.inf
  for move in get_possible_moves(state):
    new_state = make_move(state, move, 0)  # Assuming 0 is the minimizing player
    move_value = minimax(new_state, depth, True)  # Adjust depth as needed
    if move_value < best_value:
      best_move = move
      best_value = move_value
  return make_move(state, best_move, 0)

def maxer_ply(state):
  # Use minimax to find the best move for the maximizing player
  # Similar to miner_ply but with maximizing logic
  pass


def util():
    
    return


def chancer(start: int, moves: int):
    return moves + 1, moves % 2 + start


def toss():
    print(f"Its {random.randint(0, 1)}'s turn")
    return random.randint(0, 1)


def end(gameState: list[list]):
    for i in gameState:
        for j in i:
            if j ==-1:
                return False
    return True


def runner():
    player = 0
    pc = 1
    moves = 0
    maxer = 0
    miner = 0
    mm = False
    gamestate = init_state
    start = toss()
    if start == 0:
        playersymb = 0
        symbol = 1
        mm = False
    else:
        playersymb = 1
        symbol = 0
        mm = True

    while True:
        moves, playing = chancer(moves)
        if playing == player:
            posi = int(input("Enter your place"))
            gamestate[posi // 3][posi % 3] = playersymb
        else:
            if mm:
                gamestate = maxer_ply(gameState=gamestate,symbol)
            else:
                gamestate = miner_ply(gameState=gamestate,symbol)

        if end(gameState=gamestate):
            print(gamestate)
            break


if __name__ == "__main__":
    runner()
