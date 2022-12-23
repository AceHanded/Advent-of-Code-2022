"""
Day 23 puzzles of the Advent of Code (23/25).
"""


DIRECTIONAL = {"N": [(-1, -1), (0, -1), (1, -1)], "S": [(-1, 1), (0, 1), (1, 1)], "W": [(-1, 1), (-1, 0), (-1, -1)],
               "E": [(1, 1), (1, 0), (1, -1)]}


def silver():
    """The silver star solution."""
    empty_tiles = 0
    layout = []
    elves = []
    elf_positions = set()
    order = ["N", "S", "W", "E"]

    with open("day23_input.txt", "r") as input_file:
        for line in input_file:
            layout.append(line.rstrip())

    for height in range(len(layout)):
        for width in range(len(layout[0])):
            if layout[height][width] == '#':
                elves.append([(width, height), (width, height)])
                elf_positions |= {(width, height)}

    for round_ in range(10000):
        tiles = set()
        proposals = set()

        for elf in elves:
            position = elf[0]

            if all([all([(position[0] + DIRECTIONAL[direction][index][0],
                          position[1] + DIRECTIONAL[direction][index][1]) not in elf_positions for direction in order])
                    for index in range(3)]):
                continue

            for direction in order:
                if all([(position[0] + DIRECTIONAL[direction][index][0], position[1] + DIRECTIONAL[direction][index][1])
                        not in elf_positions for index in range(3)]):
                    proposal = (position[0] + DIRECTIONAL[direction][1][0], position[1] + DIRECTIONAL[direction][1][1])

                    if proposal in proposals:
                        tiles |= {proposal}
                    else:
                        proposals |= {proposal}
                        elf[1] = proposal

                    break

        for elf in elves:
            if elf[1] not in tiles:
                elf[0] = elf[1]
            else:
                elf[1] = elf[0]

        order = order[1:] + [order[0]]
        elf_positions = {elf[0] for elf in elves}

        if round_ == 9:
            x_coordinate = {elf[0][0] for elf in elves}
            y_coordinate = {elf[0][1] for elf in elves}
            empty_tiles += (max(y_coordinate) - min(y_coordinate) + 1) * \
                           (max(x_coordinate) - min(x_coordinate) + 1) - len(elf_positions)
            break

    return empty_tiles


def gold():
    """The gold star solution."""
    round_ = 0
    layout = []
    elves = []
    elf_positions = set()
    order = ["N", "S", "W", "E"]

    with open("day23_input.txt", "r") as input_file:
        for line in input_file:
            layout.append(line.rstrip())

    for height in range(len(layout)):
        for width in range(len(layout[0])):
            if layout[height][width] == '#':
                elves.append([(width, height), (width, height)])
                elf_positions |= {(width, height)}

    for round_ in range(10000):
        moved = False
        tiles = set()
        proposals = set()

        for elf in elves:
            position = elf[0]

            if all([all([(position[0] + DIRECTIONAL[direction][index][0],
                          position[1] + DIRECTIONAL[direction][index][1]) not in elf_positions for direction in order])
                    for index in range(3)]):
                continue

            for direction in order:
                if all([(position[0] + DIRECTIONAL[direction][index][0], position[1] + DIRECTIONAL[direction][index][1])
                        not in elf_positions for index in range(3)]):
                    proposal = (position[0] + DIRECTIONAL[direction][1][0], position[1] + DIRECTIONAL[direction][1][1])

                    if proposal in proposals:
                        tiles |= {proposal}
                    else:
                        proposals |= {proposal}
                        elf[1] = proposal

                    moved = True
                    break

        for elf in elves:
            if elf[1] not in tiles:
                elf[0] = elf[1]
            else:
                elf[1] = elf[0]

        order = order[1:] + [order[0]]
        elf_positions = {elf[0] for elf in elves}

        if not moved:
            round_ += 1
            break

    return round_


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
