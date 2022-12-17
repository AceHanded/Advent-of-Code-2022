"""
Day 17 puzzles of the Advent of Code (17/25).
"""


from collections import defaultdict


ROCK_SHAPES = ["-", "+", "L", "I", "cube"]


def silver():
    """The silver star solution."""
    total_height = 0
    rock_amount = 2022
    rock_index = 0
    move_index = 0
    grid_state = defaultdict(set)
    state_keys = {}

    with open("day17_input.txt", mode="r") as input_file:
        for line in input_file:
            moves = [move for move in line]

    for rock in range(rock_amount):
        grid_peaks = [0] * 7

        for key in grid_state:
            values = grid_state[key]

            for value in values:
                grid_peaks[value] = max(grid_peaks[value], key)

        peak_sum = tuple(total_height - peak for peak in grid_peaks)
        state_key = (rock_index, move_index, peak_sum)

        if state_key in state_keys:
            (previous_rock, previous_highest) = state_keys[state_key]
            cycle_count = rock - previous_rock
            remaining_cycles = (rock_amount - rock) // cycle_count
            remaining_iterations = rock_amount - (rock + cycle_count * remaining_cycles)
            additional_height = (total_height - previous_highest) * remaining_cycles

            for _ in range(remaining_iterations):
                rock_height = total_height + 4

                if ROCK_SHAPES[rock_index] == "-":
                    rock_coordinates = [(2, rock_height), (3, rock_height), (4, rock_height), (5, rock_height)]
                elif ROCK_SHAPES[rock_index] == "+":
                    rock_coordinates = [(3, rock_height + 2), (2, rock_height + 1), (3, rock_height + 1),
                                        (4, rock_height + 1), (3, rock_height)]
                elif ROCK_SHAPES[rock_index] == "L":
                    rock_coordinates = [(4, rock_height + 2), (4, rock_height + 1), (2, rock_height),
                                        (3, rock_height), (4, rock_height)]
                elif ROCK_SHAPES[rock_index] == "I":
                    rock_coordinates = [(2, rock_height + 3), (2, rock_height + 2), (2, rock_height + 1),
                                        (2, rock_height)]
                else:
                    rock_coordinates = [(2, rock_height + 1), (3, rock_height + 1), (2, rock_height), (3, rock_height)]

                rock_index = (rock_index + 1) % len(ROCK_SHAPES)

                while True:
                    if moves[move_index] == "<":
                        movement = -1
                    else:
                        movement = 1

                    move_index = (move_index + 1) % len(moves)
                    new_rock = [(rock[0] + movement, rock[1]) for rock in rock_coordinates]

                    if all(((rock[1] not in grid_state or rock[0] not in grid_state[rock[1]]) and 0 <= rock[0] < 7)
                           for rock in new_rock):
                        rock_coordinates = new_rock
                    else:
                        rock_coordinates = rock_coordinates

                    fallen_rock = [(rock[0], rock[1] - 1) for rock in rock_coordinates]

                    if all(((rock[1] not in grid_state or rock[0] not in grid_state[rock[1]]) and rock[1] > 0)
                           for rock in fallen_rock):
                        rock_coordinates = fallen_rock
                    else:
                        for rock_ in rock_coordinates:
                            grid_state[rock_[1]].add(rock_[0])
                        break

                total_height = max(grid_state.keys())

            total_height += additional_height
            break

        else:
            state_keys[state_key] = (rock, total_height)

        rock_height = total_height + 4

        if ROCK_SHAPES[rock_index] == "-":
            rock_coordinates = [(2, rock_height), (3, rock_height), (4, rock_height), (5, rock_height)]
        elif ROCK_SHAPES[rock_index] == "+":
            rock_coordinates = [(3, rock_height + 2), (2, rock_height + 1), (3, rock_height + 1),
                                (4, rock_height + 1), (3, rock_height)]
        elif ROCK_SHAPES[rock_index] == "L":
            rock_coordinates = [(4, rock_height + 2), (4, rock_height + 1), (2, rock_height),
                                (3, rock_height), (4, rock_height)]
        elif ROCK_SHAPES[rock_index] == "I":
            rock_coordinates = [(2, rock_height + 3), (2, rock_height + 2), (2, rock_height + 1),
                                (2, rock_height)]
        else:
            rock_coordinates = [(2, rock_height + 1), (3, rock_height + 1), (2, rock_height), (3, rock_height)]

        rock_index = (rock_index + 1) % len(ROCK_SHAPES)

        while True:
            if moves[move_index] == "<":
                movement = -1
            else:
                movement = 1

            move_index = (move_index + 1) % len(moves)
            new_rock = [(rock[0] + movement, rock[1]) for rock in rock_coordinates]

            if all(((rock[1] not in grid_state or rock[0] not in grid_state[rock[1]]) and 0 <= rock[0] < 7)
                   for rock in new_rock):
                rock_coordinates = new_rock
            else:
                rock_coordinates = rock_coordinates

            fallen_rock = [(rock[0], rock[1] - 1) for rock in rock_coordinates]

            if all(((rock[1] not in grid_state or rock[0] not in grid_state[rock[1]]) and rock[1] > 0)
                   for rock in fallen_rock):
                rock_coordinates = fallen_rock
            else:
                for rock_ in rock_coordinates:
                    grid_state[rock_[1]].add(rock_[0])
                break

        total_height = max(grid_state.keys())

    return total_height


def gold():
    """The gold star solution."""
    total_height = 0
    rock_amount = 1000000000000
    rock_index = 0
    move_index = 0
    grid_state = defaultdict(set)
    state_keys = {}

    with open("day17_input.txt", mode="r") as input_file:
        for line in input_file:
            moves = [move for move in line]

    for rock in range(rock_amount):
        grid_peaks = [0] * 7

        for key in grid_state:
            values = grid_state[key]

            for value in values:
                grid_peaks[value] = max(grid_peaks[value], key)

        peak_sum = tuple(total_height - peak for peak in grid_peaks)
        state_key = (rock_index, move_index, peak_sum)

        if state_key in state_keys:
            (previous_rock, previous_highest) = state_keys[state_key]
            cycle_count = rock - previous_rock
            remaining_cycles = (rock_amount - rock) // cycle_count
            remaining_iterations = rock_amount - (rock + cycle_count * remaining_cycles)
            additional_height = (total_height - previous_highest) * remaining_cycles

            for _ in range(remaining_iterations):
                rock_height = total_height + 4

                if ROCK_SHAPES[rock_index] == "-":
                    rock_coordinates = [(2, rock_height), (3, rock_height), (4, rock_height), (5, rock_height)]
                elif ROCK_SHAPES[rock_index] == "+":
                    rock_coordinates = [(3, rock_height + 2), (2, rock_height + 1), (3, rock_height + 1),
                                        (4, rock_height + 1), (3, rock_height)]
                elif ROCK_SHAPES[rock_index] == "L":
                    rock_coordinates = [(4, rock_height + 2), (4, rock_height + 1), (2, rock_height),
                                        (3, rock_height), (4, rock_height)]
                elif ROCK_SHAPES[rock_index] == "I":
                    rock_coordinates = [(2, rock_height + 3), (2, rock_height + 2), (2, rock_height + 1),
                                        (2, rock_height)]
                else:
                    rock_coordinates = [(2, rock_height + 1), (3, rock_height + 1), (2, rock_height), (3, rock_height)]

                rock_index = (rock_index + 1) % len(ROCK_SHAPES)

                while True:
                    if moves[move_index] == "<":
                        movement = -1
                    else:
                        movement = 1

                    move_index = (move_index + 1) % len(moves)
                    new_rock = [(rock[0] + movement, rock[1]) for rock in rock_coordinates]

                    if all(((rock[1] not in grid_state or rock[0] not in grid_state[rock[1]]) and 0 <= rock[0] < 7)
                           for rock in new_rock):
                        rock_coordinates = new_rock
                    else:
                        rock_coordinates = rock_coordinates

                    fallen_rock = [(rock[0], rock[1] - 1) for rock in rock_coordinates]

                    if all(((rock[1] not in grid_state or rock[0] not in grid_state[rock[1]]) and rock[1] > 0)
                           for rock in fallen_rock):
                        rock_coordinates = fallen_rock
                    else:
                        for rock_ in rock_coordinates:
                            grid_state[rock_[1]].add(rock_[0])
                        break

                total_height = max(grid_state.keys())

            total_height += additional_height
            break

        else:
            state_keys[state_key] = (rock, total_height)

        rock_height = total_height + 4

        if ROCK_SHAPES[rock_index] == "-":
            rock_coordinates = [(2, rock_height), (3, rock_height), (4, rock_height), (5, rock_height)]
        elif ROCK_SHAPES[rock_index] == "+":
            rock_coordinates = [(3, rock_height + 2), (2, rock_height + 1), (3, rock_height + 1),
                                (4, rock_height + 1), (3, rock_height)]
        elif ROCK_SHAPES[rock_index] == "L":
            rock_coordinates = [(4, rock_height + 2), (4, rock_height + 1), (2, rock_height),
                                (3, rock_height), (4, rock_height)]
        elif ROCK_SHAPES[rock_index] == "I":
            rock_coordinates = [(2, rock_height + 3), (2, rock_height + 2), (2, rock_height + 1),
                                (2, rock_height)]
        else:
            rock_coordinates = [(2, rock_height + 1), (3, rock_height + 1), (2, rock_height), (3, rock_height)]

        rock_index = (rock_index + 1) % len(ROCK_SHAPES)

        while True:
            if moves[move_index] == "<":
                movement = -1
            else:
                movement = 1

            move_index = (move_index + 1) % len(moves)
            new_rock = [(rock[0] + movement, rock[1]) for rock in rock_coordinates]

            if all(((rock[1] not in grid_state or rock[0] not in grid_state[rock[1]]) and 0 <= rock[0] < 7)
                   for rock in new_rock):
                rock_coordinates = new_rock
            else:
                rock_coordinates = rock_coordinates

            fallen_rock = [(rock[0], rock[1] - 1) for rock in rock_coordinates]

            if all(((rock[1] not in grid_state or rock[0] not in grid_state[rock[1]]) and rock[1] > 0)
                   for rock in fallen_rock):
                rock_coordinates = fallen_rock
            else:
                for rock_ in rock_coordinates:
                    grid_state[rock_[1]].add(rock_[0])
                break

        total_height = max(grid_state.keys())

    return total_height


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
