from __future__ import annotations

from enum import Enum
from typing import Tuple
from dataclasses import dataclass


class Piece(Enum):
    CROSS = "X"
    NAUGHT = "O"
    EMPTY = " "


@dataclass
class Move:
    piece: Piece
    x_coord: int
    y_coord: int

    def __post_init__(self):
        self._validate_piece()
        self._validate_coords()

    def _validate_piece(self):
        if self.piece.value not in [Piece.CROSS.value, Piece.NAUGHT.value]:
            raise ValueError("All moves must either be a O or a X. Got {0} instead".format(self.piece))

    def _validate_coords(self):
        for coord in [self.x_coord, self.y_coord]:
            if not (0 <= coord <= 2):
                raise ValueError(
                    "All coords must be between 0-2 inclusive, got ({0}, {1}) instead"
                    .format(self.x_coord, self.y_coord)
                )


@dataclass
class Square:
    piece: Piece = Piece.EMPTY

    def __str__(self):
        return self.piece.value

    def is_empty(self):
        return self.piece == Piece.EMPTY

    def add_piece(self, piece: Piece):
        if self.is_empty():
            self.piece = piece
        # Throw an error for illegal move


@dataclass
class GameBoard:
    board: Tuple[
        Tuple[Square, Square, Square],
        Tuple[Square, Square, Square],
        Tuple[Square, Square, Square],
    ]

    @staticmethod
    def create_new_board() -> GameBoard:
        return GameBoard(
            board=(
                (Square(), Square(), Square()),
                (Square(), Square(), Square()),
                (Square(), Square(), Square()),
            )
        )

    def __str__(self):
        return f" {self.board[0][0]} | {self.board[1][0]} | {self.board[2][0]} \n" \
               f" ---------- \n" \
               f" {self.board[0][1]} | {self.board[1][1]} | {self.board[2][1]} \n" \
               f" ---------- \n" \
               f" {self.board[0][2]} | {self.board[1][2]} | {self.board[2][2]}"

    def add_move(self, move: Move):
        self.board[move.x_coord][move.y_coord].add_piece(move.piece)

    def game_over(self) -> bool:
        pass

    def game_winner(self):
        pass
