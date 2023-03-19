import random

from itertools import chain, repeat, zip_longest as zipl
from typing import Tuple, Union

from engine import MainBoard, SubBoard, MainBoardCoords, SubBoardCoords


# ===== ===== ===== EXCEPTION CLASSES ===== ===== =====
class GameStateError(Exception):
    pass


class GameBoardError(Exception):
    pass


# ===== ===== ===== PLAYER CONSTANTS ===== ===== =====
ENEMY = -1
NEUTRAL = 0
ME = 1
STALEMATE = 99

# ===== ===== ===== SUPPORT FUNCTIONS ===== ===== =====
# Convert to and from indices and coordinates
def index_coords(i: Union[int, None] = None) -> Union[MainBoardCoords, None]:
    if i is None:
        return None
    return MainBoardCoords(i // 3, i % 3)


def coords_index(mb: MainBoardCoords) -> int:
    return (mb.row * 3) + mb.col


def total_index(col: int, row: int) -> int:
    return ((col % 3) * 1) + ((col // 3) * 9) + ((row % 3) * 3) + ((row // 3) * 27)


# Misc
def to_str(coords=None) -> Union[str, None]:
    if coords is None:
        return None
    return f"({coords.col}, {coords.row})"


def num_symb(num) -> str:
    try:
        return {ME: "X", ENEMY: "O", NEUTRAL: " ", STALEMATE: "#"}[num]
    except KeyError:
        raise GameBoardError("SYMBOL_ERROR") from None


# ===== ===== ===== COORDINATE CLASSES ===== ===== =====
class SingleCoords:
    def __init__(self, full) -> None:
        self.full = full if isinstance(full, int) else (full.row * 3) + full.col

    def gen_coord(self) -> SubBoardCoords:
        return SubBoardCoords(self.full // 3, self.full % 3)

    def gen_replace(self, row=None, col=None) -> int:
        return (row or self.full // 3) * 3 + (col or self.full % 3)


class DoubleCoords:
    def __init__(self, main, sub=None) -> None:
        if sub is None:
            self.main = main // 9
            self.sub = main % 9
            self.full = main
        else:
            self.main = main if isinstance(main, int) else (main.row * 3) + main.col
            self.sub = sub if isinstance(sub, int) else (sub.row * 3) + sub.col
            self.full = (self.main * 9) + self.sub

    def gen_coords(self) -> Tuple[MainBoardCoords, SubBoardCoords]:
        return (
            MainBoardCoords(self.main // 3, self.main % 3),
            SubBoardCoords(self.sub // 3, self.sub % 3),
        )

    def gen_replace(self, mr=None, mc=None, sr=None, sc=None) -> int:
        main = (mr or self.main // 3) * 3 + (mc or self.main % 3)
        sub = (sr or self.sub // 3) * 3 + (sc or self.sub % 3)
        return (main * 9) + sub


class GameState:
    def __init__(
        self, board_restriction=None, cells=None, board_wins=None, winner=None
    ) -> None:
        self._board_restriction = board_restriction
        self._cells = cells
        self._board_wins = board_wins
        self._winner = winner

    def __str__(self) -> str:
        symb = lambda col_i, col_j, row_i, row_j: num_symb(
            self._cells[total_index(col_i * 3 + col_j, row_i * 3 + row_j)]
        )
        row_divider = "========================="

        board_str_list = [
            f"BOARD RESTRICTION: {to_str(index_coords(self._board_restriction))}"
        ]
        board_str_list.extend(
            [
                "\n".join(
                    " ".join(
                        table_column
                        for table_column in chain(
                            *zipl(
                                repeat("|", 3 + 1),
                                (
                                    f"{' '.join(symb(c_i, c_j, r_i, r_j) for c_j in range(3))}"
                                    for c_i in range(3)
                                ),
                            )
                        )
                        if table_column is not None
                    )
                    for r_j in range(3)
                )
                for r_i in range(3)
            ]
        )
        board_str_list.extend(
            [
                f"| {' '.join(f'{num_symb(self._board_wins[i * 3 + j])}' for j in range(3))} |"
                for i in range(3)
            ]
        )
        return "\n".join(
            row_block
            for row_block in chain(
                *zipl(repeat(row_divider, 3 + 1 + 1), board_str_list)
            )
            if row_block is not None
        )

    # ===== ===== ===== MONTE CARLO METHODS ===== ===== =====
    def __eq__(self, other) -> bool:
        if self._winner != other._winner:
            return False
        if self._board_restriction != other._board_restriction:
            return False
        if any(a != b for a, b in zip(self._board_wins, other._board_wins)):
            return False
        if any(a != b for a, b in zip(self._cells, other._cells)):
            return False
        return True

    def __hash__(self) -> int:
        return self._cells.__hash__()

    def get_children(self) -> set:

        children = set()

        # Terminal
        if self._winner != 0:
            return children

        # All moves
        if self._board_restriction is None:
            for i in range(81):
                move = DoubleCoords(i)
                if (
                    self._board_wins[move.main] == NEUTRAL
                    and self._cells[move.full] == NEUTRAL
                ):
                    children.add(GameState(self, move))
            return children

        # Restricted moves
        for sub in range(9):
            move = DoubleCoords(self._board_restriction, sub)
            if self._cells[move.full] == NEUTRAL:
                children.add(GameState(self, move))
        return children

    def get_random_child(self) -> GameState:

        rand_offset = random.randrange(81)

        # All moves
        if self._board_restriction is None:
            for j in range(81):
                i = (rand_offset + j) % 81
                move = DoubleCoords(i)
                if (
                    self._board_wins[move.main] == NEUTRAL
                    and self._cells[move.full] == NEUTRAL
                ):
                    return GameState(self, move)
            raise GameStateError(f"{self}\nTerminal state - no children")

        # Restricted moves
        for j in range(9):
            sub = (rand_offset + j) % 9
            move = DoubleCoords(self._board_restriction, sub)
            if self._cells[move.full] == NEUTRAL:
                return GameState(self, move)
        raise GameStateError(f"{self}\nNo moves found")

    def get_move_to(self, next_coords_pair) -> Tuple[MainBoardCoords, SubBoardCoords]:
        for i in range(81):
            if bool(self._cells[i] == NEUTRAL) is not bool(
                next_coords_pair._cells[i] == NEUTRAL
            ):
                return DoubleCoords(i).gen_coords()
        raise GameStateError(f"{self}\nNo move found between states")

    def is_terminal(self) -> bool:
        return self._winner != NEUTRAL

    def board_score(self) -> int:  # Heuristic
        try:
            return {ME: 1000, ENEMY: -1000, STALEMATE: 0}[self._winner]
        except KeyError:
            return sum(self._board_wins)

    def reward(self) -> float:  # None-Heuristic
        try:
            return {NEUTRAL: 0.5, STALEMATE: 0.5, ME: 1}[self._winner]
        except KeyError:
            return 0

    # ===== ===== ===== IMPORT FROM GAMEBOARD ===== ===== =====
    @classmethod
    def from_gameboard(cls, board_input: Union[MainBoard, None] = None) -> None:
        state = {
            "board_restriction": None,
            "cells": None,
            "board_wins": None,
            "winner": None,
        }

        # BOARD RESTRICTION
        playable_coords = board_input.get_playable_coords()
        state["board_restriction"] = (
            coords_index(playable_coords[0]) if len(playable_coords) == 1 else None
        )

        # ALL CELLS
        cell_list = []
        for i in range(81):
            mb, sb = DoubleCoords(i).gen_coords()
            value = (
                board_input._board[mb.row][mb.col]
                ._board[sb.row][sb.col]
                .played_by.value
            )
            cell_list.append(ME if value == 1 else ENEMY if value == 2 else NEUTRAL)
        state["cells"] = tuple(cell_list)

        # GET FINISHED BOARDS
        state["board_wins"] = []
        for i in range(9):
            coords = index_coords(i)
            sb = board_input._board[coords.row][coords.col]
            if not sb._is_finished:
                state["board_wins"].append(NEUTRAL)
                continue
            state["board_wins"].append(ME if sb.winner.value == 1 else ENEMY)

        # GET WINNER
        if not board_input.is_finished:
            state["winner"] = NEUTRAL
        else:
            try:
                state["winner"] = {1: ME, 2: ENEMY}[board_input._winner.value]
            except KeyError:
                state["winner"] = STALEMATE

        return cls(**state)

    # ===== ===== ===== COPY FROM ANOTHER STATE ===== ===== =====
    @classmethod
    def from_gamestate(
        cls, other: GameState, move: Union[DoubleCoords, None]
    ) -> GameState:
        state = {
            "board_restriction": None,
            "cells": None,
            "board_wins": None,
            "winner": None,
        }

        # Copy data
        state["cells"] = (
            other._cells[: move.full] + (ME,) + other._cells[(move.full + 1) :]
        )  # TODO - optimise so tuple isn't being created twice
        state["board_wins"] = list(other._board_wins)
        state["winner"] = other._winner
        state["board_restriction"] = other._board_restriction

        # Make move
        cls.set_sub_winner(state, move)
        cls.set_main_winner(state, SingleCoords(move.main))
        state["board_restriction"] = (
            move.sub if state["board_wins"][move.sub] == NEUTRAL else None
        )

        # Flip values for opponent's context
        state["cells"] = tuple(-1 * element for element in state["cells"])
        state["board_wins"] = [-1 * board_win for board_win in state["board_wins"]]
        state["winner"] = -1 * state["winner"]

        return cls(**state)

    @staticmethod
    def set_sub_winner(state: dict, move: DoubleCoords):

        # Already set
        if state["board_wins"][move.main] != NEUTRAL:
            return

        # Check for new win (enemy won't have new win)
        if (
            (  # HORIZONTAL
                state["cells"][move.gen_replace(sc=0)] == ME
                and state["cells"][move.gen_replace(sc=1)] == ME
                and state["cells"][move.gen_replace(sc=2)] == ME
            )
            or (  # VERTICAL
                state["cells"][move.gen_replace(sr=0)] == ME
                and state["cells"][move.gen_replace(sr=1)] == ME
                and state["cells"][move.gen_replace(sr=2)] == ME
            )
            or (  # DIAGONAL 1
                state["cells"][move.gen_replace(sr=0, sc=0)] == ME
                and state["cells"][move.gen_replace(sr=1, sc=1)] == ME
                and state["cells"][move.gen_replace(sr=2, sc=2)] == ME
            )
            or (  # DIAGONAL 2
                state["cells"][move.gen_replace(sr=0, sc=2)] == ME
                and state["cells"][move.gen_replace(sr=1, sc=1)] == ME
                and state["cells"][move.gen_replace(sr=2, sc=0)] == ME
            )
        ):
            state["board_wins"][move.main] = ME

        # Check for remaining moves
        if any(state["cells"][(move.main * 9) + i] == NEUTRAL for i in range(9)):
            return  # leave at NEUTRAL

        # Set stalemate
        state["board_wins"][move.main] = STALEMATE

    @staticmethod
    def set_main_winner(state, move: SingleCoords):

        # Already set
        if state["winner"] != NEUTRAL:
            return

        # Check for new win (enemy won't have new win)
        if (
            (  # HORIZONTAL
                state["board_wins"][move.gen_replace(col=0)] == ME
                and state["board_wins"][move.gen_replace(col=1)] == ME
                and state["board_wins"][move.gen_replace(col=2)] == ME
            )
            or (  # VERTICAL
                state["board_wins"][move.gen_replace(row=0)] == ME
                and state["board_wins"][move.gen_replace(row=1)] == ME
                and state["board_wins"][move.gen_replace(row=2)] == ME
            )
            or (  # DIAGONAL 1
                state["board_wins"][move.gen_replace(row=0, col=0)] == ME
                and state["board_wins"][move.gen_replace(row=1, col=1)] == ME
                and state["board_wins"][move.gen_replace(row=2, col=2)] == ME
            )
            or (  # DIAGONAL 2
                state["board_wins"][move.gen_replace(row=0, col=2)] == ME
                and state["board_wins"][move.gen_replace(row=1, col=1)] == ME
                and state["board_wins"][move.gen_replace(row=2, col=0)] == ME
            )
        ):
            state["winner"] = ME

        # Check for remaining moves
        if any(board_win == NEUTRAL for board_win in state["board_wins"]):
            return  # leave at NEUTRAL

        # Set stalemate
        state["winner"] = STALEMATE
