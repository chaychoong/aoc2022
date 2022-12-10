from typing import List


class Program:
    def __init__(self) -> None:
        self.register = {"X": [1]}

    def parse_instruction(self, instruction: str) -> None:
        # each instruction goes like "addx 3" or "noop"
        match instruction.split(" ")[0]:
            case "addx":
                self.register["X"].append(self.register["X"][-1])
                self.register["X"].append(
                    self.register["X"][-1] + int(instruction.split(" ")[1])
                )
            case "noop":
                self.register["X"].append(self.register["X"][-1])


def solution_p1(input_list: List[str]) -> int:
    program = Program()
    for instruction in input_list:
        program.parse_instruction(instruction)

    for n in (20, 60, 100, 140, 180, 220):
        print(program.register["X"][n - 1])
    return sum([n * program.register["X"][n - 1] for n in (20, 60, 100, 140, 180, 220)])


def solution_p2(input_list: List[str]) -> None:
    program = Program()
    for instruction in input_list:
        program.parse_instruction(instruction)

    crt_printout = []
    for i in range(len(program.register["X"]) - 1):
        crt_position = i % 40
        sprite_position = program.register["X"][i]
        if sprite_position - 1 <= crt_position <= sprite_position + 1:
            crt_printout.append("#")
        else:
            crt_printout.append(".")

    # split crt_printout into lists of 40 elements
    crt_printout = [crt_printout[i : i + 40] for i in range(0, len(crt_printout), 40)]

    for line in crt_printout:
        print("".join(line))
