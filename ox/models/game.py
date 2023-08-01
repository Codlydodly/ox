from typing import Dict
from uuid import UUID
from dataclasses import dataclass

from models.player import Player
from models.game_board import GameBoard, Piece, Move


@dataclass
class Game:
    id: UUID
    x_player: Player
    o_player: Player
    game_board: GameBoard = GameBoard.create_new_board()

    def player_turn(self, player: Player):
        self.game_board.add_move(

        )

