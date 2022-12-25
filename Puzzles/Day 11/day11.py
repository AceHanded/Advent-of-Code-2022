"""
Day 11 puzzles of the Advent of Code (11/25).
"""


from math import lcm


def silver():
    """The silver star solution."""
    rounds = 20
    monkeys = []

    with open("day11_input.txt", mode="r") as input_file:
        data = input_file.read()

    lines = [line for line in data.strip().split("Monkey ") if len(line) > 0]

    for line in lines:
        monkey_info = line.split("\n")

        monkey = int(monkey_info[0].split(":")[0])

        items = [int(item) for item in monkey_info[1].split(": ")[1].split(", ")]

        value = monkey_info[2].split(" ")[-1]
        operator = monkey_info[2].split(" ")[-2]
        operation = create_operation_function(value, operator)

        divisor = int(monkey_info[3].split(" ")[-1])
        monkey_if_true = int(monkey_info[4].split(" ")[-1])
        monkey_if_false = int(monkey_info[5].split(" ")[-1])
        test = create_test_function(divisor, monkey_if_true, monkey_if_false)

        monkeys.append({"monkey": monkey, "items": items, "operation": operation, "test": test})

    monkey_items = {monkey["monkey"]: monkey["items"] for monkey in monkeys}
    monkey_funcs = {monkey["monkey"]: monkey["operation"] for monkey in monkeys}
    monkey_tests = {monkey["monkey"]: monkey["test"] for monkey in monkeys}
    monkey_count = {monkey["monkey"]: 0 for monkey in monkeys}

    for _ in range(rounds):
        for monkey, old_worries in monkey_items.items():
            new_worries = [monkey_funcs[monkey](worry) for worry in old_worries]
            new_worries = [worry // 3 for worry in new_worries]
            send_to = [monkey_tests[monkey](worry) for worry in new_worries]

            [monkey_items[to].append(worry) for to, worry in zip(send_to, new_worries)]

            monkey_items[monkey] = []
            monkey_count[monkey] += len(old_worries)

    inspect_counts = sorted(list(monkey_count.values()))
    active_monkey_count, active_monkey2_count = inspect_counts[-2:]
    monkey_business_level = active_monkey_count * active_monkey2_count

    return monkey_business_level


def gold():
    """The gold star solution."""
    rounds = 10000
    monkeys = []
    divisors = []

    with open("day11_input.txt", mode="r") as input_file:
        data = input_file.read()

    lines = [line for line in data.strip().split("Monkey ") if len(line) > 0]

    for line in lines:
        monkey_info = line.split("\n")

        monkey = int(monkey_info[0].split(":")[0])

        items = [int(item) for item in monkey_info[1].split(": ")[1].split(", ")]

        value = monkey_info[2].split(" ")[-1]
        operator = monkey_info[2].split(" ")[-2]
        operation = create_operation_function(value, operator)

        divisor = int(monkey_info[3].split(" ")[-1])
        divisors.append(divisor)
        monkey_if_true = int(monkey_info[4].split(" ")[-1])
        monkey_if_false = int(monkey_info[5].split(" ")[-1])
        test = create_test_function(divisor, monkey_if_true, monkey_if_false)

        monkeys.append({"monkey": monkey, "items": items, "operation": operation, "test": test})

    monkey_items = {monkey["monkey"]: monkey["items"] for monkey in monkeys}
    monkey_funcs = {monkey["monkey"]: monkey["operation"] for monkey in monkeys}
    monkey_tests = {monkey["monkey"]: monkey["test"] for monkey in monkeys}
    monkey_count = {monkey["monkey"]: 0 for monkey in monkeys}

    divisors_lowest_common_multiple = lcm(*(divisor for divisor in divisors))

    for _ in range(rounds):
        for monkey, old_worries in monkey_items.items():
            new_worries = [monkey_funcs[monkey](worry) for worry in old_worries]
            new_worries = [worry % divisors_lowest_common_multiple for worry in new_worries]
            send_to = [monkey_tests[monkey](worry) for worry in new_worries]

            [monkey_items[to].append(worry) for to, worry in zip(send_to, new_worries)]

            monkey_items[monkey] = []
            monkey_count[monkey] += len(old_worries)

    inspect_counts = sorted(list(monkey_count.values()))
    active_monkey_count, active_monkey2_count = inspect_counts[-2:]
    monkey_business_level = active_monkey_count * active_monkey2_count

    return monkey_business_level


def create_operation_function(value, operator):
    """Creates a lambda function for calculating the heightened worry level."""
    if value == "old":
        return lambda x: x + x if operator == "+" else x * x
    else:
        return lambda x: x + int(value) if operator == "+" else x * int(value)


def create_test_function(divisor, monkey_if_true, monkey_if_false):
    """Creates a lambda function for calculating whether the current worry level is
    divisible by the divisor."""
    return lambda x: monkey_if_true if x % divisor == 0 else monkey_if_false


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
