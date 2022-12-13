import itertools
from functools import cmp_to_key
from typing import List


def compare_pairs(item1, item2):
    if type(item1) == int and type(item2) == int:
        # return -1 if item1 < item2, 0 if item1 == item2, 1 if item1 > item2
        return (item1 > item2) - (item1 < item2)

    if type(item1) == int and type(item2) == list:
        return compare_pairs([item1], item2)

    if type(item1) == list and type(item2) == int:
        return compare_pairs(item1, [item2])

    if type(item1) == list and type(item2) == list:
        for i in range(len(item1)):
            try:
                result = compare_pairs(item1[i], item2[i])
                if result == 0:
                    continue
                return result
            except IndexError:
                return 1

        if len(item1) == len(item2):
            return 0

        if len(item1) < len(item2):
            return -1

    return 1


def parse_inp_list(inp_list: List[str]):
    # split list into smaller lists, for every item containing '' (empty string)
    iterator = itertools.groupby(inp_list, lambda x: x == "")
    inp_list_split = [list([eval(item) for item in g]) for k, g in iterator if not k]
    return inp_list_split


def solution_p1(inp_list: List[str]) -> int:
    parsed_pairs = parse_inp_list(inp_list)
    right_order_tracker = []

    for i in range(len(parsed_pairs)):
        if compare_pairs(parsed_pairs[i][0], parsed_pairs[i][1]) == -1:
            right_order_tracker.append(i + 1)

    print(right_order_tracker)
    return sum(right_order_tracker)


def solution_p2(inp_list: List[str]) -> int:
    marker1 = [[2]]
    marker2 = [[6]]
    # remove all "" in inp_list
    inp_list = [eval(item) for item in inp_list if item != ""]
    inp_list.extend([marker1, marker2])
    inp_list = sorted(inp_list, key=cmp_to_key(compare_pairs))
    for i in range(len(inp_list)):
        print(inp_list[i])

    return (inp_list.index(marker1) + 1) * (inp_list.index(marker2) + 1)
