from typing import List


def _read_input_lines() -> List[str]:
    with open("src/day1/input.txt") as f:
        lines = f.read().splitlines()

    return lines


def _get_elves_calories_from_lines(lines: List[str]) -> List[List[int]]:
    elves_calories: List[List[int]] = []
    current_elf: List[int] = []
    for line in lines:
        if line == "":
            elves_calories.append(current_elf)
            current_elf = []
            continue

        current_elf.append(int(line))

    elves_calories.append(current_elf)
    return elves_calories


def _compute_elves_total_calories(elves_calories: List[List[int]]) -> List[int]:
    return [sum(calories) for calories in elves_calories]


def _compute_sum_top_3_calories() -> int:
    lines = _read_input_lines()
    elves_calories = _get_elves_calories_from_lines(lines)
    elves_total_calories = _compute_elves_total_calories(elves_calories)

    sorted_total_calories = sorted(elves_total_calories, reverse=True)
    return sum(sorted_total_calories[:3])


def main() -> None:
    print(_compute_sum_top_3_calories())
