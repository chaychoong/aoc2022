from typing import List

DIRECTION_ENUM = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def add_tuples(t1, t2):
    return tuple(map(lambda x, y: x + y, t1, t2))


def subtract_tuples(t1, t2):
    return tuple(map(lambda x, y: x - y, t1, t2))


class World:
    def __init__(self):
        self.current_direction = (0, 0)

    def set_direction(self, new_direction: str):
        self.current_direction = DIRECTION_ENUM[new_direction]


class Knot:
    def __init__(self, world: World, parent: "Knot" = None, name=None):
        self.position = (0, 0)
        self.world = world
        self.parent = parent
        if parent is not None:
            self.parent.child = self

        self.child = None
        self.name = name

        self.adjacent_points = []
        self.set_adjacent_points(point=(0, 0))

        self.visited_points = set({(0, 0)})

    def move(self, direction=None):
        if direction is None:
            self.position = add_tuples(self.position, self.world.current_direction)
        else:
            self.position = add_tuples(self.position, direction)

        self.visited_points.add(self.position)
        self.set_adjacent_points()

        if self.child is not None and self.position not in self.child.adjacent_points:
            parent_direction = subtract_tuples(self.position, self.child.position)

            # normalize direction
            parent_direction_normalized = (
                parent_direction[0] // abs(parent_direction[0])
                if parent_direction[0] != 0
                else 0,
                parent_direction[1] // abs(parent_direction[1])
                if parent_direction[1] != 0
                else 0,
            )

            self.child.move(parent_direction_normalized)

    def set_adjacent_points(self, point=None):
        if point is None:
            point = self.position

        self.adjacent_points = [
            point,
            (point[0] - 1, point[1]),
            (point[0] - 1, point[1] - 1),
            (point[0] - 1, point[1] + 1),
            (point[0] + 1, point[1]),
            (point[0] + 1, point[1] + 1),
            (point[0] + 1, point[1] - 1),
            (point[0], point[1] - 1),
            (point[0], point[1] + 1),
        ]

    def get_num_visited(self):
        return len(self.visited_points)


def solution_p1(input_list: List[str]) -> int:
    world = World()
    knot_list = [Knot(world=world, name="head")]

    for i in range(1, 2):
        knot_list.append(Knot(world=world, parent=knot_list[-1], name=f"child_{i}"))

    for line in input_list:
        # each line goes like "R 4"
        direction, distance = line[0], int(line[1:])
        world.set_direction(direction)
        for _ in range(distance):
            knot_list[0].move()

    return knot_list[-1].get_num_visited()


def solution_p2(input_list: List[str]) -> int:
    world = World()
    knot_list = [Knot(world=world, name="head")]

    for i in range(1, 10):
        knot_list.append(Knot(world=world, parent=knot_list[-1], name=f"child_{i}"))

    for line in input_list:
        # each line goes like "R 4"
        direction, distance = line[0], int(line[1:])
        world.set_direction(direction)
        for _ in range(distance):
            knot_list[0].move()

    return knot_list[-1].get_num_visited()
