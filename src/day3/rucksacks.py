from typing import List, Tuple

Rucksack = Tuple[str, str]


def _find_misplaced_item(rucksask: Rucksack) -> str:
    (first, second) = rucksask
    common_items = set(first).intersection(set(second))
    if len(common_items) != 1:
        raise ValueError("List should have a single common item")

    return common_items.pop()


def _get_item_priority(item: str) -> int:
    order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return order.index(item) + 1


def sum_misplaced_item_priorities(rucksasks: List[Rucksack]) -> int:
    priority_sum = 0
    for rucksask in rucksasks:
        misplaced = _find_misplaced_item(rucksask)
        priority = _get_item_priority(misplaced)
        priority_sum += priority

    return priority_sum


def load_rucksacks() -> List[Rucksack]:
    with open("src/day3/input.txt") as f:
        lines = f.read().splitlines()

    output: List[Rucksack] = []
    for line in lines:
        half = len(line) // 2
        output.append((line[0:half], line[half:]))
    return output
