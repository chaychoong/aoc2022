def parse_input_list(input_list: list[str]):
    index = input_list.index("")

    return input_list[:index], input_list[index + 1 :]


def parse_stack(stack_raw: list[str]) -> list[str]:
    # columns are like " 1   2   3 "
    # so we need to split on spaces and remove empty strings
    stack_col = list(filter(None, stack_raw[-1].split(" ")))

    # initialise stacks array based on the size of stack_col
    stacks = [[] for _ in range(len(stack_col))]

    for col in stack_raw[-2::-1]:
        for i in range(len(stacks)):
            # index is 1, 5, 9
            # the formula is 4 * i + 1
            # append item unless it's a space, then don't append
            item = col[4 * i + 1]
            if item != " ":
                stacks[i].append(col[4 * i + 1])

    return stacks


def parse_instructions(
    instructions_raw: list[str], stacks: list[list[str]], preserve_order: bool = False
) -> list[str]:
    instructions = []

    for instruction in instructions_raw:
        # instruction is in the format "move 1 from 2 to 1"
        # split on spaces and remove empty strings
        split_instructons = instruction.split(" ")
        num_to_move = int(split_instructons[1])
        from_stack = int(split_instructons[3]) - 1
        to_stack = int(split_instructons[5]) - 1

        if preserve_order:
            # create a temp stack to hold the items we want to move
            temp_stack = []
            for _ in range(num_to_move):
                temp_stack.append(stacks[from_stack].pop())

            # move the items from the temp stack to the destination stack
            stacks[to_stack].extend(temp_stack[-1::-1])
        else:
            for _ in range(num_to_move):
                stacks[to_stack].append(stacks[from_stack].pop())

    # merge the last item in each stack into a single string
    return "".join([stack[-1] for stack in stacks])


def solution_p1(input_list: list[str]) -> str:
    # find index of item with "" in it
    stack_raw, instructions_raw = parse_input_list(input_list)

    stacks = parse_stack(stack_raw)
    return parse_instructions(instructions_raw, stacks)


def solution_p2(input_list: list[str]) -> str:
    # find index of item with "" in it
    stack_raw, instructions_raw = parse_input_list(input_list)

    stacks = parse_stack(stack_raw)
    return parse_instructions(instructions_raw, stacks, preserve_order=True)
