from typing import Callable, List


class Monkey:
    # optimisation for part 2
    # (a mod kn) mod n = a mod n
    # therefore we can combine the modulo tests from all the monkeys into one giant modulo test
    # the weakness of this method is that this is a singleton, meaning we have to "reset" it on every run
    # plus, we can't run this in parallel
    # meh, screw it
    shared_modulo: int = 1
    monkey_list: List["Monkey"] = []

    def get_monkey_business():
        active_list = [monkey.inspect_count for monkey in Monkey.monkey_list]
        active_list.sort(reverse=True)
        return active_list[0] * active_list[1]

    def operate_on_all_monkeys():
        for monkey in Monkey.monkey_list:
            monkey.operate_on_list()

    def __init__(
        self,
        name: str,
        items: List[int],
        operation: Callable,
        test: int,
        if_true_monkey_index: int,
        if_false_monkey_index: int,
        worry_level_divisor: int,
    ):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true_monkey_index = if_true_monkey_index
        self.if_false_monkey_index = if_false_monkey_index
        self.inspect_count = 0
        self.worry_level_divisor = worry_level_divisor

        Monkey.shared_modulo *= test

    def operate_on_list(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            result = self.operation(item)
            result = result // self.worry_level_divisor
            if result % self.test == 0:
                Monkey.monkey_list[self.if_true_monkey_index].items.append(
                    result % Monkey.shared_modulo
                )
            else:
                Monkey.monkey_list[self.if_false_monkey_index].items.append(
                    result % Monkey.shared_modulo
                )
            self.inspect_count += 1

    def from_inp_str(
        name_inp: str,
        items_inp: str,
        operation_inp: str,
        test_inp: str,
        true_inp: str,
        false_inp: str,
        worry_level_divisor: int,
    ) -> "Monkey":
        # name is in the form "Monkey 0:"
        name = name_inp.split()[1][:-1]

        # items is in the form "  Starting items: 79, 98"
        items = [int(i) for i in items_inp.split(":")[1].split(",")]

        # operation_inp is in the form "  Operation: new = old * 19"
        operation = eval(f"lambda old: {operation_inp.split('new = ')[1]}")

        # test is in the form "  Test: divisible by 23"
        test = int(test_inp.split()[3])

        # true_inp is in the form "    If true: throw to monkey 2"
        if_true_monkey_index = int(true_inp.split()[5])

        # false_inp is in the form "    If false: throw to monkey 3"
        if_false_monkey_index = int(false_inp.split()[5])

        return Monkey(
            name,
            items,
            operation,
            test,
            if_true_monkey_index,
            if_false_monkey_index,
            worry_level_divisor,
        )


def init_monkey_list(inp: List[str], worry_level_divisor: int) -> List[Monkey]:
    Monkey.shared_modulo = 1
    Monkey.monkey_list = []
    # split inp into list of 7
    split_inp = [inp[i : i + 7] for i in range(0, len(inp), 7)]
    for group in split_inp:
        # create Monkey from group
        Monkey.monkey_list.append(Monkey.from_inp_str(*group[:6], worry_level_divisor))


def solution_p1(inp: List[str]) -> int:
    init_monkey_list(inp, 3)

    for _ in range(20):
        Monkey.operate_on_all_monkeys()

    return Monkey.get_monkey_business()


def solution_p2(inp: List[str]) -> int:
    init_monkey_list(inp, 1)

    for _ in range(10000):
        Monkey.operate_on_all_monkeys()

    return Monkey.get_monkey_business()
