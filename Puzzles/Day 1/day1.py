"""
Day 1 puzzles of the Advent of Code.
"""


def silver():
    calories = []
    total_calories = 0

    with open("day1_input.txt", mode="r") as input_file:
        for line in input_file:
            if line != "\n":
                total_calories += int(line)
            else:
                calories.append(total_calories)
                total_calories = 0

    max_calories = max(calories)

    return max_calories


def gold():
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

    for value in range(0, 3):
        max_calories += max(calories)
        calories.pop(calories.index(max(calories)))

    return max_calories


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
