import csv
from dataclasses import dataclass
from typing import List

from src.day2.move import Move


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


def _parse_personal_move(value: str) -> Move:
    match value:
        case "X":
            return Move.ROCK
        case "Y":
            return Move.PAPER
        case "Z":
            return Move.SCISSOR
        case _:
            raise ValueError(f"Unknown personal move {value}")


def read_rounds() -> List[Round]:
    output: List[Round] = []
    with open("src/day2/input.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        for opponent, me in reader:
            opponent_move = _parse_move_from_opponent(opponent)
            personal_move = _parse_personal_move(me)
            output.append(Round(opponent_move, personal_move))

    return output
