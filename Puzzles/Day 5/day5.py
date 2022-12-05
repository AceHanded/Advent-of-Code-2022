"""
Day 5 puzzles of the Advent of Code.
"""


def silver():
    """The silver star solution."""
    top_crates = ""
    crates = {"1": ["Q", "F", "M", "R", "L", "W", "C", "V"], "2": ["D", "Q", "L"],
              "3": ["P", "S", "R", "G", "W", "C", "N", "B"], "4": ["L", "C", "D", "H", "B", "Q", "G"],
              "5": ["V", "G", "L", "F", "Z", "S"], "6": ["D", "G", "N", "P"], "7": ["D", "Z", "P", "V", "F", "C", "W"],
              "8": ["C", "P", "D", "M", "S"], "9": ["Z", "N", "W", "T", "V", "M", "P", "C"]}

    with open("day5_input.txt", mode="r") as input_file:
        for line in input_file:
            if line.startswith("move"):
                line = line.rstrip()
                amount, from_, to = line.split(" ")[1::2]

                for times in range(0, int(amount)):
                    crates[to].append(crates[from_][-1])
                    del crates[from_][-1]

        for key in crates:
            top_crates += crates[key][-1]

    return top_crates


def gold():
    """The gold star solution."""
    top_crates = ""
    crates = {"1": ["Q", "F", "M", "R", "L", "W", "C", "V"], "2": ["D", "Q", "L"],
              "3": ["P", "S", "R", "G", "W", "C", "N", "B"], "4": ["L", "C", "D", "H", "B", "Q", "G"],
              "5": ["V", "G", "L", "F", "Z", "S"], "6": ["D", "G", "N", "P"], "7": ["D", "Z", "P", "V", "F", "C", "W"],
              "8": ["C", "P", "D", "M", "S"], "9": ["Z", "N", "W", "T", "V", "M", "P", "C"]}

    with open("day5_input.txt", mode="r") as input_file:
        for line in input_file:
            if line.startswith("move"):
                line = line.rstrip()
                amount, from_, to = line.split(" ")[1::2]

                crates[to].extend(crates[from_][len(crates[from_]) - int(amount):len(crates[from_])])
                del crates[from_][len(crates[from_]) - int(amount):len(crates[from_])]

        for key in crates:
            top_crates += crates[key][-1]

    return top_crates


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
