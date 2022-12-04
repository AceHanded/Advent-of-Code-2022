"""
Day 2 puzzles of the Advent of Code.
"""


LOSS = 0
DRAW = 3
WIN = 6


def read_file(gold=None):
    total_points = 0

    if gold:
        moves = {"A": {"X": LOSS+3, "Y": DRAW+1, "Z": WIN+2},
                 "B": {"X": LOSS+1, "Y": DRAW+2, "Z": WIN+3},
                 "C": {"X": LOSS+2, "Y": DRAW+3, "Z": WIN+1}}
    else:
        moves = {"A": {"X": DRAW+1, "Y": WIN+2,  "Z": LOSS+3},
                 "B": {"X": LOSS+1, "Y": DRAW+2, "Z": WIN+3},
                 "C": {"X": WIN+1,  "Y": LOSS+2, "Z": DRAW+3}}

    with open("day2_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()
            opponent, you = line.split(" ")

            total_points += moves[opponent][you]

        return total_points


def main():
    silver = read_file()
    gold = read_file(gold=True)
    print(f"Silver: {silver}\nGold: {gold}")


if __name__ == "__main__":
    main()