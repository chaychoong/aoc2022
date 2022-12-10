INDEX_MAP = {
    # them
    "A": 0,  # rock
    "B": 1,  # paper
    "C": 2,  # scissors
    # us
    "X": 0,  # rock / lose
    "Y": 1,  # paper / draw
    "Z": 2,  # scissors / win
}

SCORE_TABLE_1 = (  # for each row: we throw R/P/S
    (3 + 1, 6 + 2, 0 + 3),  # they throw R. we D/W/L
    (0 + 1, 3 + 2, 6 + 3),  # they throw P. we L/D/W
    (6 + 1, 0 + 2, 3 + 3),  # they throw S. we W/L/D
)


SCORE_TABLE_2 = (  # for each row: we have to L/D/W
    (0 + 3, 3 + 1, 6 + 2),  # they throw R. we throw S/R/P
    (0 + 1, 3 + 2, 6 + 3),  # they throw P. we throw R/P/S
    (0 + 2, 3 + 3, 6 + 1),  # they throw S. we throw P/S/R
)


def get_score(them: str, us: str, lookup_table):
    # look up score table and calculate score
    return lookup_table[INDEX_MAP[them]][INDEX_MAP[us]]


def process_matches(matches: str, lookup_table):
    sum = 0

    # matches is a string of space separated matchup "them us"
    for match in matches:
        them, us = match.split(" ")
        sum += get_score(them, us, lookup_table)

    return sum


def solution_p1(matches):
    return process_matches(matches, SCORE_TABLE_1)


def solution_p2(matches):
    return process_matches(matches, SCORE_TABLE_2)
