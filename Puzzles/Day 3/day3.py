"""
Day 3 puzzles of the Advent of Code (3/25).
"""


CHARS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
         "S", "T", "U", "V", "W", "X", "Y", "Z"]


def silver():
    """The silver star solution."""
    total_priority = 0

    with open("day3_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]

            for character in first_half:
                if character in [*second_half]:
                    total_priority += CHARS.index(character) + 1
                    break

    return total_priority


def gold():
    """The gold star solution."""
    total_priority = 0
    lines = []

    with open("day3_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            if len(lines) != 3:
                lines.append(line)
            else:
                total_priority += find_common_character(lines)

                lines = [line]

        total_priority += find_common_character(lines)

    return total_priority


def find_common_character(lines):
    """Finds the common character in three subsequent character groups."""
    priority = 0

    for line in lines:
        for character in line:
            if character in lines[0] and character in lines[1] and character in lines[2]:
                priority = CHARS.index(character) + 1
                break

    return priority


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
