"""
Day 10 puzzles of the Advent of Code (10/25).
"""


def silver():
    """The silver star solution."""
    register_x = 1
    total_cycles = 0
    check_cycle = 20
    total_signal_strengths = 0

    with open("day10_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            if line == "noop":
                total_cycles += 1

                if total_cycles == check_cycle:
                    signal_strength = check_cycle * register_x
                    total_signal_strengths += signal_strength
                    check_cycle += 40

            else:
                split_line = line.split()
                addx_value = split_line[1]

                for _ in range(0, 2):
                    total_cycles += 1

                    if total_cycles == check_cycle:
                        signal_strength = check_cycle * register_x
                        total_signal_strengths += signal_strength
                        check_cycle += 40

                register_x += int(addx_value)

    return total_signal_strengths


def gold():
    """The gold star solution."""
    register_x = 1
    total_cycles = 0
    check_cycle = 20
    total_signal_strengths = 0
    crt_screen_row = ""
    crt_screen_rows = []

    with open("day10_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            if line == "noop":
                total_cycles += 1

                if total_cycles == check_cycle:
                    signal_strength = check_cycle * register_x
                    total_signal_strengths += signal_strength
                    check_cycle += 40

                if abs((total_cycles - 1) % 40 - register_x) < 2:
                    crt_screen_row += "#"
                else:
                    crt_screen_row += "."

                if len(crt_screen_row) == 40:
                    crt_screen_rows.append(crt_screen_row)
                    crt_screen_row = ""

            else:
                split_line = line.split()
                addx_value = split_line[1]

                for _ in range(0, 2):
                    total_cycles += 1

                    if total_cycles == check_cycle:
                        signal_strength = check_cycle * register_x
                        total_signal_strengths += signal_strength
                        check_cycle += 40

                    if abs((total_cycles - 1) % 40 - register_x) < 2:
                        crt_screen_row += "#"
                    else:
                        crt_screen_row += "."

                    if len(crt_screen_row) == 40:
                        crt_screen_rows.append(crt_screen_row)
                        crt_screen_row = ""

                register_x += int(addx_value)

    display = "\n".join(crt_screen_rows)

    return f"\n{display}"


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
