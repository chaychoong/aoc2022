import os

from day10.solution import solution_p1, solution_p2
from utils.get_input import get_input_as_list
from utils.timing import timeit

BASE_FOLDER = os.path.basename(os.path.dirname(__file__))


@timeit
def test_part1():
    assert solution_p1(get_input_as_list(f"{BASE_FOLDER}/example2.txt")) == 13140
    print(solution_p1(get_input_as_list(f"{BASE_FOLDER}/puzzle.txt")))


@timeit
def test_part2():
    print(solution_p2(get_input_as_list(f"{BASE_FOLDER}/example2.txt")))
    print()
    print(solution_p2(get_input_as_list(f"{BASE_FOLDER}/puzzle.txt")))
