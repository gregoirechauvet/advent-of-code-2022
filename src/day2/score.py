from typing import List

from src.day2.move import Move
from src.day2.round import Round


def _get_shape_score(move: Move) -> int:
    match move:
        case Move.ROCK:
            return 1
        case Move.PAPER:
            return 2
        case Move.SCISSOR:
            return 3


def _get_round_score(round: Round) -> int:
    if round.is_win():
        return 6
    if round.is_draw():
        return 3
    return 0


def compute_score(rounds: List[Round]) -> int:
    total = 0
    for round in rounds:
        total += _get_shape_score(round.me) + _get_round_score(round)
    return total
