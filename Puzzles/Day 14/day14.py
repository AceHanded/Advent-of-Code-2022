"""
Day 14 puzzles of the Advent of Code (14/25).
"""


def silver():
    """The silver star solution."""
    total_units = 0
    max_row = 0
    source = (0, 500)
    sand_can_fall = True
    lines = []
    rock = {}

    with open("day14_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip().split(" -> ")

            lines.append([[int(position.split(',')[0]), int(position.split(',')[1])] for position in line])

    for line in lines:
        for rock_index in range(1, len(line)):
            first_row = int(line[rock_index - 1][1])
            first_column = int(line[rock_index - 1][0])
            second_row = int(line[rock_index][1])
            second_column = int(line[rock_index][0])
            if first_row > max_row:
                max_row = first_row
            if second_row > max_row:
                max_row = second_row
            elif first_row == second_row:
                if first_column > second_column:
                    first_column, second_column = second_column, first_column
                for column in range(first_column, second_column + 1):
                    rock[(first_row, column)] = 1
            else:
                if first_row > second_row:
                    first_row, second_row = second_row, first_row
                for row in range(first_row, second_row + 1):
                    rock[(row, first_column)] = 1

    for position in range(500 - max_row - 10, 500 + max_row + 10):
        rock[(max_row + 2, position)] = 1

    while sand_can_fall:
        rest = source

        while True:
            down, down_left, down_right = (rest[0] + 1, rest[1]), (rest[0] + 1, rest[1] - 1), (rest[0] + 1, rest[1] + 1)
            if down not in rock:
                rest = down
                continue
            elif down_left not in rock:
                rest = down_left
                continue
            elif down_right not in rock:
                rest = down_right
                continue

            rock[rest] = 2
            if rest[0] > max_row:
                sand_can_fall = False
                break

            total_units += 1
            break

    return total_units


def gold():
    """The gold star solution."""
    total_units = 0
    max_row = 0
    source = (0, 500)
    sand_can_fall = True
    lines = []
    rock = {}

    with open("day14_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip().split(" -> ")

            lines.append([[int(position.split(',')[0]), int(position.split(',')[1])] for position in line])

    for line in lines:
        for index in range(1, len(line)):
            first_row = line[index - 1][1]
            first_column = line[index - 1][0]
            second_row = line[index][1]
            second_column = line[index][0]
            if first_row > max_row:
                max_row = first_row
            if second_row > max_row:
                max_row = second_row
            elif first_row == second_row:
                if first_column > second_column:
                    first_column, second_column = second_column, first_column
                for column in range(first_column, second_column + 1):
                    rock[(first_row, column)] = 1
            else:
                if first_row > second_row:
                    first_row, second_row = second_row, first_row
                for row in range(first_row, second_row + 1):
                    rock[(row, first_column)] = 1

    for position in range(500 - max_row - 10, 500 + max_row + 10):
        rock[(max_row + 2, position)] = 1

    while sand_can_fall:
        if source in rock:
            total_units -= 1
            sand_can_fall = False

        rest = source

        while True:
            down, down_left, down_right = (rest[0] + 1, rest[1]), (rest[0] + 1, rest[1] - 1), (rest[0] + 1, rest[1] + 1)
            if down not in rock:
                rest = down
                continue
            elif down_left not in rock:
                rest = down_left
                continue
            elif down_right not in rock:
                rest = down_right
                continue

            rock[rest] = 2
            if rest[0] > max_row:
                total_units += 1
                break

            total_units += 1
            break

    return total_units


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
