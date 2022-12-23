"""
Day 22 puzzles of the Advent of Code (22/25).
"""


TURNS = {'R': 1, 'L': -1, '': 0}
DIRECTIONAL = [1, 1j, -1, -1j]


def silver():
    """The silver star solution."""
    password = 0
    lines = ""
    symbols = ""
    tiles = {}
    instructions = []
    start = 0
    width = 1
    depth = 1

    with open("day22_input.txt", "r") as input_file:
        for line in input_file:
            lines += line

    path = lines.split("\n\n")

    for y_coordinate, row in enumerate(path[0].splitlines(), 1):
        depth = max(depth, y_coordinate)

        for x_coordinate, tile in enumerate(row, 1):
            width = max(width, x_coordinate)

            if not start and tile == '.':
                start = x_coordinate + y_coordinate * 1j
            elif tile != ' ':
                tiles[x_coordinate + y_coordinate * 1j] = tile

    for instruction in path[1]:
        if instruction.isdigit():
            symbols += instruction
        else:
            instructions.append((symbols, instruction))
            symbols = ""

    instructions.append((symbols, ""))

    position = start
    facing = 0

    for (steps, turn) in instructions:
        for _ in range(int(steps)):
            new_tile = position
            new_tile += DIRECTIONAL[facing]

            while new_tile not in tiles:
                new_tile += DIRECTIONAL[facing]
                x_coordinate = new_tile.real

                if x_coordinate < 1:
                    x_coordinate = width
                elif x_coordinate > width:
                    x_coordinate = 1

                y_coordinate = new_tile.imag

                if y_coordinate < 1:
                    y_coordinate = depth
                elif y_coordinate > depth:
                    y_coordinate = 1

                new_tile = x_coordinate + y_coordinate * 1j

            if tiles[new_tile] == '.':
                position = new_tile
            else:
                break

        facing = (facing + TURNS[turn]) % 4

    password += int(1000 * position.imag + 4 * position.real + facing)

    return password


def gold():
    """The gold star solution."""
    password = 0
    lines = ""
    symbols = ""
    tiles = {}
    instructions = []
    start = 0
    width = 1
    depth = 1

    with open("day22_input.txt", "r") as input_file:
        for line in input_file:
            lines += line

    path = lines.split("\n\n")

    for y_coordinate, row in enumerate(path[0].splitlines(), 1):
        depth = max(depth, y_coordinate)

        for x_coordinate, tile in enumerate(row, 1):
            width = max(width, x_coordinate)

            if not start and tile == '.':
                start = x_coordinate + y_coordinate * 1j
            elif tile != ' ':
                tiles[x_coordinate + y_coordinate * 1j] = tile

    for instruction in path[1]:
        if instruction.isdigit():
            symbols += instruction
        else:
            instructions.append((symbols, instruction))
            symbols = ""

    instructions.append((symbols, ""))

    position = start
    facing = 0
    new_facing = 0

    for (steps, turn) in instructions:
        for _ in range(int(steps)):
            new_tile = position
            new_tile += DIRECTIONAL[facing]
            switch = False

            if new_tile not in tiles:
                switch = True

                if facing == 0:
                    if 1 <= new_tile.imag <= 50:
                        x_coordinate = 100
                        y_coordinate = 151 - new_tile.imag
                        new_facing = 2
                    elif 51 <= new_tile.imag <= 100:
                        x_coordinate = 50 + new_tile.imag
                        y_coordinate = 50
                        new_facing = 3
                    elif 101 <= new_tile.imag <= 150:
                        x_coordinate = 150
                        y_coordinate = 51 - (new_tile.imag - 100)
                        new_facing = 2
                    else:
                        x_coordinate = 50 + (new_tile.imag - 150)
                        y_coordinate = 150
                        new_facing = 3
                elif facing == 1:
                    if 101 <= new_tile.real <= 150:
                        x_coordinate = 100
                        y_coordinate = 50 + (new_tile.real - 100)
                        new_facing = 2
                    elif 51 <= new_tile.real <= 100:
                        x_coordinate = 50
                        y_coordinate = 150 + (new_tile.real - 50)
                        new_facing = 2
                    else:
                        x_coordinate = new_tile.real + 100
                        y_coordinate = new_tile.imag - 200
                        new_facing = facing
                elif facing == 2:
                    if 1 <= new_tile.imag <= 50:
                        x_coordinate = 1
                        y_coordinate = 151 - new_tile.imag
                        new_facing = 0
                    elif 51 <= new_tile.imag <= 100:
                        x_coordinate = new_tile.imag - 50
                        y_coordinate = 101
                        new_facing = 1
                    elif 101 <= new_tile.imag <= 150:
                        x_coordinate = 51
                        y_coordinate = 151 - new_tile.imag
                        new_facing = 0
                    else:
                        x_coordinate = 50 + (new_tile.imag - 150)
                        y_coordinate = 1
                        new_facing = 1
                else:
                    if 1 <= new_tile.real <= 50:
                        x_coordinate = 51
                        y_coordinate = 50 + new_tile.real
                        new_facing = 0
                    elif 51 <= new_tile.real <= 100:
                        x_coordinate = 1
                        y_coordinate = 100 + new_tile.real
                        new_facing = 0
                    else:
                        x_coordinate = new_tile.real - 100
                        y_coordinate = 200
                        new_facing = facing

                new_tile = x_coordinate + y_coordinate * 1j

            if tiles[new_tile] == '.':
                position = new_tile

                if switch:
                    facing = new_facing
            else:
                break

        facing = (facing + TURNS[turn]) % 4

    password += int(1000 * position.imag + 4 * position.real + facing)

    return password


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
