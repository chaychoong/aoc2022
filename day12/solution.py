from collections import deque
from typing import List


class Point:
    def __init__(self, coord_x: int, coord_y: int, height: int):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.height = height

    def __repr__(self) -> str:
        return f"({self.coord_x}, {self.coord_y})"


class HeightMap:
    def __init__(self):
        self.map_list: List[List[Point]] = []
        self.start = None
        self.end = None

    def parse_map_inp(self, inp_list: List[str]):
        start_coord = None
        end_coord = None
        for y in range(len(inp_list)):
            tmp_col: List[Point] = []
            for x in range(len(inp_list[y])):
                char = inp_list[y][x]
                if char == "S":
                    char_to_int = 97
                    start_coord = (x, y)
                elif char == "E":
                    char_to_int = 122
                    end_coord = (x, y)
                else:
                    char_to_int = ord(char)

                tmp_col.append(Point(x, y, char_to_int))

            self.map_list.append(tmp_col)

        self.start = self.get_point(*start_coord)
        self.end = self.get_point(*end_coord)

    def get_point(self, coord_x: int, coord_y: int) -> Point:
        if (
            coord_x < 0
            or coord_y < 0
            or coord_y >= len(self.map_list)
            or coord_x >= len(self.map_list[0])
        ):
            return None
        return self.map_list[coord_y][coord_x]

    # BFS from end to start
    def get_shortest_path_from_start(self) -> int:
        queue = deque([(self.start,)])
        visited = set([self.start])

        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == self.end:
                return path

            for neighbour in [
                self.get_point(node.coord_x, node.coord_y + 1),
                self.get_point(node.coord_x, node.coord_y - 1),
                self.get_point(node.coord_x + 1, node.coord_y),
                self.get_point(node.coord_x - 1, node.coord_y),
            ]:
                if neighbour is None:
                    continue
                if neighbour.height - node.height > 1:
                    continue
                if neighbour in visited:
                    continue
                queue.append((path + (neighbour,)))
                visited.add(neighbour)

    def get_shortest_path_to_A_from_end(self) -> int:
        queue = deque([(self.end,)])
        visited = set([self.end])

        while queue:
            path = queue.popleft()
            node = path[-1]

            # check if we are at A
            if node.height == 97:
                return path

            for neighbour in [
                self.get_point(node.coord_x, node.coord_y + 1),
                self.get_point(node.coord_x, node.coord_y - 1),
                self.get_point(node.coord_x + 1, node.coord_y),
                self.get_point(node.coord_x - 1, node.coord_y),
            ]:
                if neighbour is None:
                    continue
                # we are doing the inverse this time
                if node.height - neighbour.height > 1:
                    continue
                if neighbour in visited:
                    continue
                queue.append((path + (neighbour,)))
                visited.add(neighbour)


def solution_p1(inp_list: List[str]) -> int:
    height_map = HeightMap()
    height_map.parse_map_inp(inp_list)
    shortest_path = height_map.get_shortest_path_from_start()
    return len(shortest_path) - 1


def solution_p2(inp_list: List[str]) -> int:
    height_map = HeightMap()
    height_map.parse_map_inp(inp_list)
    shortest_path = height_map.get_shortest_path_to_A_from_end()
    return len(shortest_path) - 1
