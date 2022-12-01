import os

from day2.solution import solution_p1, solution_p2
from utils.get_input import get_input_as_list

BASE_FOLDER = os.path.basename(os.path.dirname(__file__))


def test_part1():
    assert solution_p1(get_input_as_list(f"{BASE_FOLDER}/example.txt")) == 15
    print(solution_p1(get_input_as_list(f"{BASE_FOLDER}/puzzle.txt")))


def test_part2():
    assert solution_p2(get_input_as_list(f"{BASE_FOLDER}/example.txt")) == 12
    print(solution_p2(get_input_as_list(f"{BASE_FOLDER}/puzzle.txt")))
