"""
When creating a game code returns "draw" immediately and asks to play again.
"""
import itertools as it
import numpy as np
from string import ascii_uppercase as letters

PLAYER_SYMBOL = ("O", "X")

def update_board(boardsize, state, scores):
    board_width = 2 * (boardsize + 1) + 1
    score_width = 7 + sum(len(str(score)) for score in scores)
    indent = " " * ((board_width - score_width) // 2)

    board = [
        indent + f" {' - '.join(map(str, scores))} ".join(PLAYER_SYMBOL),
        *(f"{boardsize - i} {''.join(state[i])}|" for i in range(boardsize)),
        f"  {''.join(f'|{letter}' for letter in letters[:boardsize])}|",
    ]
    print(f"\n{'-' * board_width}\n".join(board))

    
def get_possible(boardsize, state, current_player):
    possible = []
    # Search board for current player's symbol
    np.argwhere(state == f"|{PLAYER_SYMBOL[current_player]}")
    for i, j in it.product(range(boardsize), repeat=2):
        if state[i][j] != f"|{PLAYER_SYMBOL[current_player]}":
            continue
        # Checking bordering spaces
        for x, y in it.product((-1, 0, 1), repeat=2):
            # Ignore current space or indices outside of the boardsize
            if (x == 0 and y == 0) or (
                i + x not in range(boardsize) or j + y not in range(boardsize)
            ):
                continue
            if state[i + x][j + y] in (f"|{PLAYER_SYMBOL[1 - current_player]}", "| "):
                if f"{letters[j + y]}{boardsize - i - x}" not in possible:
                    possible.append(f"{letters[j + y]}{boardsize - i - x}")
    return possible

def print_outcome(scores):
    if scores[0] > scores[1]:
        print("Player 1 wins.")
    elif scores[1] > scores[0]:
        print("Player 2 wins.")
    else:
        print("Draw.")

def player_turn(boardsize, state, possible, scores, current_player):
    print(
        f"Player {current_player + 1}'s turn. "
        "Choose a move among the following possible moves: \n"
        f"{possible}"
    )
    while True:
        if (choice := input("Enter choice: ")) in possible:
            break
        print("Invalid choice.")
    letter, num = choice
    xc = -int(num)
    yc = letters.find(letter)
    scores[current_player] += 1
    if state[xc][yc] == f"|{PLAYER_SYMBOL[1 - current_player]}":
        scores[1 - current_player] -= 1
        state[xc][yc] = "|■"
    else:
        state[xc][yc] = f"|{PLAYER_SYMBOL[current_player]}"

def play_game(boardsize, state, scores):
    current_player = 0
    while True:
        update_board(boardsize, state, scores)
        if not (possible := get_possible(boardsize, state, current_player)):
            break
        player_turn(boardsize, state, possible, scores, current_player)
        current_player = 1 - current_player
    print("Game Over.")
    print_outcome(scores)

def main():
    while True:
        try:
            boardsize = int(input("Please enter the desired board size: "))
        except ValueError:
            print("Invalid board size.")
        else:
            break

    while True:
        state = np.full((boardsize, boardsize), "| ")
        state[0][-1] = "|X"
        state[-1][0] = "|O"
        scores = [np.sum(state == f"|{symbol}") for symbol in PLAYER_SYMBOL]
        
        play_game(boardsize, state, scores)
        ans = input("Do you want to start again? y/n\n").lower()
        if not ans.startswith("y"):
            break

if __name__ == "__main__":
    main()