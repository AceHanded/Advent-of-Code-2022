"""
Day 24 puzzles of the Advent of Code (24/25).
"""


import heapq


def silver():
    """The silver star solution."""
    minutes = 0
    layout = []

    with open("day24_input.txt", "r") as input_file:
        for line in input_file:
            layout.append(line.strip())

    start = (1, 0)
    goal = len(layout[-1]) - 2, len(layout) - 1

    minutes += search(layout, start, goal)

    return minutes


def gold():
    """The gold star solution."""
    minutes = 0
    layout = []

    with open("day24_input.txt", "r") as input_file:
        for line in input_file:
            layout.append(line.strip())

    start = (1, 0)
    goal = len(layout[-1]) - 2, len(layout) - 1

    minutes += search(layout, start, goal, search(layout, goal, start, search(layout, start, goal)))

    return minutes


def search(layout, start, goal, minutes=0):
    """Searches for the fewest number of minutes required to reach the goal."""
    x_final, y_final = goal
    visited, queue = {(start, minutes)}, [(0, (start, minutes))]

    while queue:
        position, minutes = heapq.heappop(queue)[1]

        if position == goal:
            return minutes

        x_coordinate, y_coordinate = position
        minutes += 1

        for x_coordinate, y_coordinate in [(x_coordinate - 1, y_coordinate), (x_coordinate, y_coordinate - 1),
                                           (x_coordinate, y_coordinate), (x_coordinate, y_coordinate + 1),
                                           (x_coordinate + 1, y_coordinate)]:
            if y_coordinate < 0 or y_coordinate >= len(layout) or x_coordinate < 1 or \
                    x_coordinate >= len(row := layout[y_coordinate]) - 1:
                continue

            if y_coordinate in (0, len(layout) - 1):
                if row[x_coordinate] != ".":
                    continue
            elif layout[y_coordinate][(x_coordinate - 1 + minutes) % (len(row) - 2) + 1] == "<" or \
                    layout[y_coordinate][(x_coordinate - 1 - minutes) % (len(row) - 2) + 1] == ">" or \
                    layout[(y_coordinate - 1 + minutes) % (len(layout) - 2) + 1][x_coordinate] == "^" or \
                    layout[(y_coordinate - 1 - minutes) % (len(layout) - 2) + 1][x_coordinate] == "v":
                continue

            state = ((x_coordinate, y_coordinate), minutes)

            if state not in visited:
                visited.add(state)
                heapq.heappush(queue, (minutes + abs(x_coordinate - x_final) + abs(y_coordinate - y_final), state))


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
