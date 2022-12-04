"""
Day 1 puzzles of the Advent of Code.
"""


def read_file(gold=None):
    calories = []
    total_calories = 0
    max_calories = 0

    with open("day1_input.txt", mode="r") as input_file:
        for line in input_file:
            if line != "\n":
                total_calories += int(line)
            else:
                calories.append(total_calories)
                total_calories = 0

    if gold:
        for value in range(0, 3):
            max_calories += max(calories)
            calories.pop(calories.index(max(calories)))

    else:
        max_calories = max(calories)

    return max_calories


def main():
    silver = read_file()
    gold = read_file(gold=True)
    print(f"Silver: {silver}\nGold: {gold}")


if __name__ == "__main__":
    main()
