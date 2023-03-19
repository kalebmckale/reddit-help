import random
from collections import Counter
from itertools import chain, repeat, zip_longest as zipl


def generate_table(num_rows, num_columns):
    COLUMN_SEPARATOR = "|"
    ROW_SEPARATOR = f" {' '.join(repeat('---', num_columns))}"
    COLUMN_TEMPLATE = " @ "
    ROW_TEMPLATE = "".join(
        table_column
        for table_column in chain(
            *zipl(
                repeat(COLUMN_SEPARATOR, num_columns + 1),
                repeat(COLUMN_TEMPLATE, num_columns),
            )
        )
        if table_column is not None
    )
    return "\n".join(
        table_row
        for table_row in chain(
            *zipl(
                repeat(ROW_SEPARATOR, num_rows + 1),
                repeat(ROW_TEMPLATE, num_rows),
            )
        )
        if table_row is not None
    )


def score_game(game, winner_score=3):
    player_to_score = {"X": 1, "O": -1}
    score_to_player = {score: player for player, score in player_to_score.items()}
    scores = [
        [player_to_score[column.strip()] for column in row.split("|") if column]
        for row in game.split("\n")
        if "-" not in row
    ]

    # Diagonal sums
    if any(is_win :=
        ((
            total := abs(
                signed := sum(
                    column
                    for row_idx, row in enumerate(score_table)
                    for col_idx, column in enumerate(row)
                    if row_idx == col_idx
                )
            )
        )
        == winner_score
        for score_table in (scores, scores[::-1]))
    ):
        print(list(is_win))
        return score_to_player[signed // total]

    # Column sums
    is_win = []
    for column in zip(*scores):
        signed = sum(column)
        total = abs(signed)
        is_win.append(total == winner_score)
    print(is_win)
    if any(is_win):
        return
    if any(is_win := ((total := abs(signed := sum(column))) == winner_score for column in zip(*scores))):
        print(list(is_win))
        return score_to_player[signed // total]

    # Row sums
    if any(is_win := ((total := abs(signed := sum(row))) == winner_score for row in scores)):
        print(list(is_win))
        return score_to_player[signed // total]

    return None


def generate_plays(num_X, num_O):
    plays = list(chain(repeat("O", num_O), repeat("X", num_X)))
    random.shuffle(plays)
    return plays


def calculate_statistics(num_games):
    outcomes = Counter(score_game(generate_game()) for game in range(num_games))
    win_rates = {player: outcomes[player] / num_games for player in ("X", "O", None)}
    return outcomes, win_rates


def generate_game(num_rows=3, num_columns=3, num_X=5, num_O=4):
    if num_rows * num_columns != num_O + num_X:
        err_msg = (
            f"num_X + num_O must equal number of elements of "
            f"table ({num_columns * num_rows}): "
            f"{num_X + num_O} given"
        )
        raise ValueError(err_msg)

    game = generate_table(num_rows, num_columns)
    for play in generate_plays(num_X, num_O):
        game = game.replace("@", play, 1)

    return game
