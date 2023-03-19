from itertools import chain, repeat, zip_longest as zipl

DEFAULT_SCORE = 3
DEFAULT_ROWS = 3
DEFAULT_COLUMNS = 3

def create_board_template(num_rows, num_columns, labels=False):
    COLUMN_SEPARATOR = "|"
    ROW_SEPARATOR = " ".join(repeat("---", num_columns))
    COLUMN_TEMPLATE = " @ "
    ROW_TEMPLATE = COLUMN_SEPARATOR.join(repeat(COLUMN_TEMPLATE, num_columns))
    HEADER_TEMPLATE = None
    if labels:
        ROW_SEPARATOR = f"  {ROW_SEPARATOR}"
        ROW_TEMPLATE = f"R {ROW_TEMPLATE}"
        HEADER_TEMPLATE = "".join(
            f"   {column_idx + 1}" for column_idx in range(num_columns)
        )

    return "\n".join(
        board_row
        for board_row in chain(
            *zipl(
                [HEADER_TEMPLATE],
                (
                    ROW_TEMPLATE.replace("R", f"{row_idx + 1}")
                    for row_idx in range(num_rows)
                ),
                repeat(ROW_SEPARATOR, num_rows - 1),
            )
        )
        if board_row is not None
    )


class TicTacToe:
    _player_symbol = {1: "X", -1: "O"}
    _flat = False
    _labels = True

    def __init__(self, num_rows=None, num_columns=None):
        rows = num_rows or DEFAULT_ROWS
        columns = num_columns or DEFAULT_COLUMNS
        self._winner_score = DEFAULT_SCORE
        self._template = create_board_template(rows, columns, self._labels)

        if self._flat:
            self._board = list(repeat(0, rows * columns))
        else:
            self._board = list(repeat(list(repeat(0, columns)), rows))

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        if self._flat:
            plays = self._board
        else:
            plays = sum(self._board, [])
        board = self._template
        for position_idx, player_id in enumerate(plays):
            try:
                board = board.replace("@", self._player_symbol[player_id], 1)
            except KeyError:
                board = board.replace(
                    "@", " " if self._labels else f"{position_idx + 1}", 1
                )
        return board

    def check_board(self):
        """
        Returns player_id if player has won.
        """
        # Implementation check for self._flat
        if self._flat:
            err_msg = f"{self.__class__.__name__}.check_board() currently requires _flat set to 'False'"
            raise NotImplementedError(err_msg)

        # Column sums
        for column in zip(*self._board):
            if (score := abs(signed := sum(column))) == self._winner_score:
                return signed // score  # Returns 1 or -1

        # Row sums
        for row in self._board:
            if (score := abs(signed := sum(column))) == self._winner_score:
                return signed // score  # Returns 1 or -1

        # Diagonal sums
        for board_choice in (self._board, self._board[::-1]):
            for row_idx, row in enumerate(board_choice):
                for col_idx, column in enumerate(row):
                    if (
                        row_idx == col_idx
                        and (score := abs(signed := sum(column))) == self._winner_score
                    ):
                        return signed // score  # Returns 1 or -1

        return None
