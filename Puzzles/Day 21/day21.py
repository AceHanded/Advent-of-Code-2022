"""
Day 21 puzzles of the Advent of Code (21/25).
"""


MONKEYS = {}


def silver():
    """The silver star solution."""
    root_number = 0

    with open("day21_input.txt", "r") as input_file:
        for line in input_file:
            name, value = line.strip().split(": ")

            if len(value.split(" ")) > 1:
                MONKEYS[name] = value.split(" ")
            else:
                MONKEYS[name] = int(value)

    root_number += int(monkey_evaluation("root"))

    return root_number


def gold():
    """The gold star solution."""
    root_number = 0

    with open("day21_input.txt", "r") as input_file:
        for line in input_file:
            name, value = line.strip().split(": ")

            if name == "humn":
                MONKEYS[name] = 1j
            else:
                if len(value.split(" ")) > 1:
                    MONKEYS[name] = value.split(" ")
                else:
                    MONKEYS[name] = int(value)

    result, result2 = monkey_complex_evaluation(MONKEYS["root"][0]), monkey_complex_evaluation(MONKEYS["root"][2])
    root_number += int((result.real - result2.real) / (result2.imag - result.imag))

    return root_number


def monkey_evaluation(monkey):
    """Evaluates the values of monkeys."""
    if isinstance(MONKEYS[monkey], int):
        return MONKEYS[monkey]

    name, operator, name2 = MONKEYS[monkey]
    MONKEYS[monkey] = eval(f'monkey_evaluation("{name}") {operator} monkey_evaluation("{name2}")')

    return MONKEYS[monkey]


def monkey_complex_evaluation(monkey):
    """Evaluates the values of monkeys, utilizing complex numbers."""
    if isinstance(MONKEYS[monkey], (int, complex)):
        return MONKEYS[monkey]

    name, operator, name2 = MONKEYS[monkey]
    MONKEYS[monkey] = eval(f'monkey_complex_evaluation("{name}") {operator} monkey_complex_evaluation("{name2}")')

    return MONKEYS[monkey]


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
