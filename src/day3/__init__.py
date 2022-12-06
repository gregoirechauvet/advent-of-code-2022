from src.day3.rucksacks import load_rucksacks, sum_misplaced_item_priorities


def main() -> None:
    rucksacks = load_rucksacks()
    print(sum_misplaced_item_priorities(rucksacks))
