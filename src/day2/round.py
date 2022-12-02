import csv
from dataclasses import dataclass
from enum import Enum, auto
from typing import List

from src.day2.move import Move, WIN_ORDER


class Outcome(Enum):
    LOSE = auto()
    DRAW = auto()
    WIN = auto()


@dataclass
class Round:
    opponent: Move
    me: Move

    def is_draw(self) -> bool:
        return self.me == self.opponent

    def is_win(self) -> bool:
        return (
            (self.me == Move.ROCK and self.opponent == Move.SCISSOR)
            or (self.me == Move.PAPER and self.opponent == Move.ROCK)
            or (self.me == Move.SCISSOR and self.opponent == Move.PAPER)
        )


def _parse_move_from_opponent(value: str) -> Move:
    match value:
        case "A":
            return Move.ROCK
        case "B":
            return Move.PAPER
        case "C":
            return Move.SCISSOR
        case _:
            raise ValueError(f"Unknown opponent move {value}")


def _parse_outcome(value: str) -> Outcome:
    match value:
        case "X":
            return Outcome.LOSE
        case "Y":
            return Outcome.DRAW
        case "Z":
            return Outcome.WIN
        case _:
            raise ValueError(f"Unknown outcome {value}")


def _get_outcome_move_offset(outcome: Outcome) -> int:
    match outcome:
        case Outcome.WIN:
            return -1
        case Outcome.DRAW:
            return 0
        case Outcome.LOSE:
            return 1


def _compute_move_from_outcome(opponent_move: Move, outcome: Outcome) -> Move:
    opponent_index = WIN_ORDER.index(opponent_move)
    move_offset = _get_outcome_move_offset(outcome)
    return WIN_ORDER[(opponent_index + move_offset) % len(WIN_ORDER)]


def read_rounds() -> List[Round]:
    output: List[Round] = []
    with open("src/day2/input.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        for opponent, raw_outcome in reader:
            opponent_move = _parse_move_from_opponent(opponent)
            outcome = _parse_outcome(raw_outcome)
            personal_move = _compute_move_from_outcome(opponent_move, outcome)
            output.append(Round(opponent_move, personal_move))

    return output
