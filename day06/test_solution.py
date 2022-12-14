import os

from day06.solution import solution_p1, solution_p2
from utils.get_input import get_input_as_list
from utils.timing import timeit

BASE_FOLDER = os.path.basename(os.path.dirname(__file__))


@timeit
def test_part1():
    assert solution_p1(get_input_as_list(f"{BASE_FOLDER}/example.txt")) == [
        7,
        5,
        6,
        10,
        11,
    ]
    print(solution_p1(get_input_as_list(f"{BASE_FOLDER}/puzzle.txt")))


@timeit
def test_part2():
    assert solution_p2(get_input_as_list(f"{BASE_FOLDER}/example.txt")) == [
        19,
        23,
        23,
        29,
        26,
    ]
    print(solution_p2(get_input_as_list(f"{BASE_FOLDER}/puzzle.txt")))
