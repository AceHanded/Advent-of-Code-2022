"""
Day 25 puzzles of the Advent of Code (25/25).
"""


SNAFU_DIGITS = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
SNAFU_CONVERSION = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}


def silver():
    """The silver star solution."""
    total_value = 0
    additional = 0
    converted_number = ""
    lines = []

    with open("day25_input.txt", "r") as input_file:
        for line in input_file:
            lines.append(line.strip())

    for line in lines:
        for index, digit in enumerate(line[::-1]):
            total_value += pow(5, index) * SNAFU_DIGITS[digit]

    while total_value != 0 or additional:
        remainder = total_value % 5 + additional
        additional = 0

        if remainder > 2:
            additional = 1

        converted_number = SNAFU_CONVERSION[remainder] + converted_number
        total_value //= 5

    return converted_number


def gold():
    """The gold star solution."""
    message = "Smoothie acquired!"

    return message


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
