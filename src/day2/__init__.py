from src.day2.round import read_rounds
from src.day2.score import compute_score


def get_total_score() -> int:
    rounds = read_rounds()
    return compute_score(rounds)


def main() -> None:
    print(get_total_score())
