from typing import List


# Given a string, define a sliding window of size 4 and print the index of the first window that contains unique characters
def return_marker_position(input: str, start_of_message_size: int) -> int:
    for i in range(len(input) - 3):
        if len(set(input[i : i + start_of_message_size])) == start_of_message_size:
            return i + start_of_message_size


def solution_p1(input: List[str]) -> List[int]:
    return [return_marker_position(line, 4) for line in input]


def solution_p2(input: List[str]) -> List[int]:
    return [return_marker_position(line, 14) for line in input]
