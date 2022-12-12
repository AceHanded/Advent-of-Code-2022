"""
Day 9 puzzles of the Advent of Code (9/25).
"""


DIRECTIONAL = {'L': (-1, 0), 'R': (1, 0), 'D': (0, -1), 'U': (0, 1)}


def silver():
    """The silver star solution."""
    moves = []
    rope_length = 2

    with open("day9_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()
            direction, distance = line.split()

            moves.append((DIRECTIONAL[direction], int(distance)))

    x_start = [0] * rope_length
    y_start = [0] * rope_length
    visited_positions = {(x_start[-1], y_start[-1])}

    for (x_move, y_move), distance in moves:
        for _ in range(distance):
            x_start[0] += x_move
            y_start[0] += y_move

            for position in range(rope_length - 1):
                x_change = x_start[position + 1] - x_start[position]
                y_change = y_start[position + 1] - y_start[position]

                if abs(x_change) == 2 or abs(y_change) == 2:
                    x_start[position + 1] = x_start[position] + int(x_change / 2)
                    y_start[position + 1] = y_start[position] + int(y_change / 2)

            visited_positions.add((x_start[-1], y_start[-1]))

    total_visited_positions = len(visited_positions)

    return total_visited_positions


def gold():
    """The gold star solution."""
    moves = []
    rope_length = 10

    with open("day9_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()
            direction, distance = line.split()

            moves.append((DIRECTIONAL[direction], int(distance)))

    x_start = [0] * rope_length
    y_start = [0] * rope_length
    visited_positions = {(x_start[-1], y_start[-1])}

    for (x_move, y_move), distance in moves:
        for _ in range(distance):
            x_start[0] += x_move
            y_start[0] += y_move

            for position in range(rope_length - 1):
                x_total = x_start[position + 1] - x_start[position]
                y_total = y_start[position + 1] - y_start[position]

                if abs(x_total) == 2 or abs(y_total) == 2:
                    x_start[position + 1] = x_start[position] + int(x_total / 2)
                    y_start[position + 1] = y_start[position] + int(y_total / 2)

            visited_positions.add((x_start[-1], y_start[-1]))

    total_visited_positions = len(visited_positions)

    return total_visited_positions


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
