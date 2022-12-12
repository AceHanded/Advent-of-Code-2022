"""
Day 12 puzzles of the Advent of Code (12/25).
"""


DIRECTIONAL = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def silver():
    """The silver star solution."""
    total_steps = 0
    grid = []

    with open("day12_input.txt", mode="r") as input_file:
        for line in input_file:
            line = list(map(ord, line.rstrip()))

            grid.append(line)

    grid_width, grid_height = len(grid[0]), len(grid)
    start, end = [[(height, width) for width in range(grid_width) for height in range(grid_height) if
                   grid[height][width] == position][0] for position in (ord("S"), ord("E"))]

    grid[start[0]][start[1]] = ord("a")
    grid[end[0]][end[1]] = ord("z")

    queue = [(0, end)]
    visited_positions = set()

    while True:
        steps, position = queue.pop(0)

        if position in visited_positions:
            continue

        visited_positions.add(position)
        current_height, current_width = position

        if grid[current_height][current_width] == ord("a") and position == start:
            total_steps += steps
            break

        for height_change, width_change in DIRECTIONAL:
            new_height, new_width = current_height + height_change, current_width + width_change

            if 0 <= new_height < grid_height and 0 <= new_width < grid_width and (new_height, new_width) not in \
                    visited_positions and (grid[current_height][current_width] - grid[new_height][new_width]) <= 1:
                queue.append((steps + 1, (new_height, new_width)))

    return total_steps


def gold():
    """The gold star solution."""
    total_steps = 0
    grid = []

    with open("day12_input.txt", mode="r") as input_file:
        for line in input_file:
            line = list(map(ord, line.rstrip()))

            grid.append(line)

    grid_width, grid_height = len(grid[0]), len(grid)
    start, end = [[(height, width) for width in range(grid_width) for height in range(grid_height) if
                   grid[height][width] == position][0] for position in (ord("S"), ord("E"))]

    grid[start[0]][start[1]] = ord("a")
    grid[end[0]][end[1]] = ord("z")

    queue = [(0, end)]
    visited_positions = set()

    while True:
        steps, position = queue.pop(0)

        if position in visited_positions:
            continue

        visited_positions.add(position)
        current_height, current_width = position

        if grid[current_height][current_width] == ord("a"):
            if not total_steps:
                total_steps += steps
            else:
                break

        for height_change, width_change in DIRECTIONAL:
            new_height, new_width = current_height + height_change, current_width + width_change

            if 0 <= new_height < grid_height and 0 <= new_width < grid_width and (new_height, new_width) not in \
                    visited_positions and (grid[current_height][current_width] - grid[new_height][new_width]) <= 1:
                queue.append((steps + 1, (new_height, new_width)))

    return total_steps


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
