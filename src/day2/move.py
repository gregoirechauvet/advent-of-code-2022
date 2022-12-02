from enum import Enum, auto


class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSOR = auto()


WIN_ORDER = [Move.PAPER, Move.ROCK, Move.SCISSOR]
