from typing import List


def parse_grid(grid: List[str]) -> List[List[int]]:
    return [[int(x) for x in row] for row in grid]


def solution_p1(input_list: List[str]) -> int:
    grid_rows = parse_grid(input_list)

    # convert rows to columns
    grid_columns = list(zip(*grid_rows))

    # initialise a grid of zeros
    grid_markers = [
        [0 for _ in range(len(grid_columns))] for _ in range(len(grid_rows))
    ]

    for x in range(len(grid_rows)):
        # from left to right
        max_height = -1
        for y in range(len(grid_columns)):
            if grid_rows[x][y] > max_height:
                max_height = grid_rows[x][y]
                grid_markers[x][y] = 1

        # from right to left
        scenic_score_counter = 0
        max_height = -1
        for y in range(len(grid_columns) - 1, -1, -1):
            if grid_rows[x][y] > max_height:
                max_height = grid_rows[x][y]
                grid_markers[x][y] = 1

    for y in range(len(grid_columns)):
        # from top to bottom
        max_height = -1
        for x in range(len(grid_rows)):
            if grid_columns[y][x] > max_height:
                max_height = grid_columns[y][x]
                grid_markers[x][y] = 1

        # from bottom to top
        max_height = -1
        for x in range(len(grid_rows) - 1, -1, -1):
            if grid_columns[y][x] > max_height:
                max_height = grid_columns[y][x]
                grid_markers[x][y] = 1

    return sum(sum(row) for row in grid_markers)


def solution_p2(input_list: List[str]) -> int:
    grid_rows = parse_grid(input_list)

    # convert rows to columns
    grid_columns = list(zip(*grid_rows))

    # initialise a grid of ones
    grid_score = [[1 for _ in range(len(grid_columns))] for _ in range(len(grid_rows))]

    # deep copy grid_score
    grid_score_left = [row[:] for row in grid_score]
    grid_score_right = [row[:] for row in grid_score]
    grid_score_up = [row[:] for row in grid_score]
    grid_score_down = [row[:] for row in grid_score]

    for x in range(len(grid_rows)):
        # look left
        last_seen_dict = {}
        prev = None
        for y in range(len(grid_columns)):
            current = grid_rows[x][y]
            if prev == None:
                grid_score_left[x][y] = 0
            elif current > prev:
                # look up last seen dict, and find the max val of a key that is equal or higher than current value
                last_blocked = max(
                    (v for k, v in last_seen_dict.items() if k >= current),
                    default=0,
                )
                grid_score_left[x][y] = y - last_blocked
            else:
                grid_score_left[x][y] = 1

            prev = grid_rows[x][y]
            last_seen_dict[prev] = y

        # look right
        last_seen_dict = {}
        prev = None
        for y in range(len(grid_columns) - 1, -1, -1):
            current = grid_rows[x][y]
            if prev == None:
                grid_score_right[x][y] = 0
            elif current > prev:
                # look up last seen dict, and find the min val of a key that is equal or higher than current value
                last_blocked = min(
                    (v for k, v in last_seen_dict.items() if k >= current),
                    default=len(grid_columns) - 1,
                )
                grid_score_right[x][y] = last_blocked - y
            else:
                grid_score_right[x][y] = 1

            prev = grid_rows[x][y]
            last_seen_dict[prev] = y

    for y in range(len(grid_columns)):
        # look up
        last_seen_dict = {}
        prev = None
        for x in range(len(grid_rows)):
            current = grid_columns[y][x]
            if prev == None:
                grid_score_up[x][y] = 0
            elif current > prev:
                # look up last seen dict, and find the max val of a key that is equal or higher than current value
                last_blocked = max(
                    (v for k, v in last_seen_dict.items() if k >= current),
                    default=0,
                )
                grid_score_up[x][y] = x - last_blocked
            else:
                grid_score_up[x][y] = 1

            prev = grid_columns[y][x]
            last_seen_dict[prev] = x

        # look down
        last_seen_dict = {}
        prev = None
        for x in range(len(grid_rows) - 1, -1, -1):
            current = grid_columns[y][x]
            if prev == None:
                grid_score_down[x][y] = 0
            elif current > prev:
                # look up last seen dict, and find the min val of a key that is equal or higher than current value
                last_blocked = min(
                    (v for k, v in last_seen_dict.items() if k >= current),
                    default=len(grid_rows) - 1,
                )
                grid_score_down[x][y] = last_blocked - x
            else:
                grid_score_down[x][y] = 1

            prev = grid_columns[y][x]
            last_seen_dict[prev] = x

    # add all the scores together
    for x in range(len(grid_rows)):
        for y in range(len(grid_columns)):
            grid_score[x][y] = (
                grid_score_left[x][y]
                * grid_score_right[x][y]
                * grid_score_up[x][y]
                * grid_score_down[x][y]
            )

    # return highest score in the grid
    return max(max(row) for row in grid_score)
