"""
Day 6 puzzles of the Advent of Code.
"""


def silver():
    """The silver star solution."""
    first_marker = 0
    subsequent_characters = []

    with open("day6_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            for character in line:
                if character in subsequent_characters:
                    subsequent_characters = [character]
                else:
                    subsequent_characters.append(character)

                    if len(subsequent_characters) == 4:
                        break

                first_marker += 1

    return first_marker


def gold():
    """The gold star solution."""
    first_marker = 0
    subsequent_characters = []

    with open("day6_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            for character in line:
                if character in subsequent_characters:
                    subsequent_characters = [character]
                    first_marker += 1
                else:
                    subsequent_characters.append(character)
                    first_marker += 1

                    if len(subsequent_characters) == 14:
                        break

    return first_marker


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
