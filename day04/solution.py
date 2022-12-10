from typing import Tuple


def is_fully_contained(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    return range1[0] >= range2[0] and range1[1] <= range2[1]


def parse_item_into_ranges(item: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    # item is in the format "1-3,5-7"
    ranges = item.split(",")
    range1 = tuple(map(int, ranges[0].split("-")))
    range2 = tuple(map(int, ranges[1].split("-")))

    return range1, range2


def solution_p1(item_list: list[str]) -> int:
    sum = 0
    for item in item_list:
        r1, r2 = parse_item_into_ranges(item)
        if is_fully_contained(r1, r2) or is_fully_contained(r2, r1):
            sum += 1

    return sum


# part 2


def is_overlapping(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    return range1[0] <= range2[0] <= range1[1] or range2[0] <= range1[0] <= range2[1]


def solution_p2(item_list: list[str]) -> int:
    sum = 0
    for item in item_list:
        r1, r2 = parse_item_into_ranges(item)
        if is_overlapping(r1, r2):
            sum += 1

    return sum
