from typing import List, Tuple

PRIORITY_LOOKUP = {k: v + 1 for v, k in enumerate("abcdefghijklmnopqrstuvwxyz")} | {
    k: v + 27 for v, k in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
}


def split_rucksack(rucksack: str) -> Tuple[str, str]:
    compartment_size = len(rucksack) // 2
    return rucksack[:compartment_size], rucksack[compartment_size:]


def get_common_item_in_two_lists(list1: List[str], list2: List[str]) -> str:
    for item in list1:
        if item in list2:
            return item


def get_common_item_in_three_lists(
    list1: List[str], list2: List[str], list3: List[str]
) -> str:
    for item in list1:
        if item in list2 and item in list3:
            return item


def sum_common_priorities_in_rucksack(rucksack: str) -> int:
    compartment1, compartment2 = split_rucksack(rucksack)
    return PRIORITY_LOOKUP[get_common_item_in_two_lists(compartment1, compartment2)]


def solution_p1(rucksacks: List[str]) -> int:
    return sum(sum_common_priorities_in_rucksack(rucksack) for rucksack in rucksacks)


# Part 2


def get_common_item_in_three_lists(
    list1: List[str], list2: List[str], list3: List[str]
) -> str:
    for item in list1:
        if item in list2 and item in list3:
            return item


def solution_p2(rucksacks: List[str]) -> int:
    rucksacks_split = [
        [list(r) for r in rucksacks[i : i + 3]] for i in range(0, len(rucksacks), 3)
    ]

    return sum(
        PRIORITY_LOOKUP[get_common_item_in_three_lists(*rucksack)]
        for rucksack in rucksacks_split
    )
