import os

from day1.solution import get_most_calories, get_most_calories_top3
from utils.get_input import get_input_as_list
from utils.timing import timeit

BASE_FOLDER = os.path.basename(os.path.dirname(__file__))


@timeit
def test_part1():
    assert get_most_calories(get_input_as_list(f"{BASE_FOLDER}/example.txt")) == 24000
    print(get_most_calories(get_input_as_list(f"{BASE_FOLDER}/puzzle.txt")))


@timeit
def test_part2():
    assert (
        get_most_calories_top3(get_input_as_list(f"{BASE_FOLDER}/example.txt")) == 45000
    )
    print(get_most_calories_top3(get_input_as_list(f"{BASE_FOLDER}/puzzle.txt")))
