"""
Day 18 puzzles of the Advent of Code (18/25).
"""


def silver():
    """The silver star solution."""
    total_area = 0
    droplet = set()

    with open("day18_input.txt", mode="r") as input_file:
        for line in input_file:
            droplet.add(tuple(map(int, line.split(","))))

    total_area += 6 * len(droplet)
    min_value = min(min(point) for point in droplet) - 1
    max_value = max(max(point) for point in droplet) + 1

    for cube in droplet:
        x_coordinate, y_coordinate, z_coordinate = cube
        examined_sides = set()

        if x_coordinate > min_value:
            examined_sides.add((x_coordinate - 1, y_coordinate, z_coordinate))
        if x_coordinate < max_value:
            examined_sides.add((x_coordinate + 1, y_coordinate, z_coordinate))
        if y_coordinate > min_value:
            examined_sides.add((x_coordinate, y_coordinate - 1, z_coordinate))
        if y_coordinate < max_value:
            examined_sides.add((x_coordinate, y_coordinate + 1, z_coordinate))
        if z_coordinate > min_value:
            examined_sides.add((x_coordinate, y_coordinate, z_coordinate - 1))
        if z_coordinate < max_value:
            examined_sides.add((x_coordinate, y_coordinate, z_coordinate + 1))

        total_area -= len(examined_sides & droplet)

    return total_area


def gold():
    """The gold star solution."""
    total_area = 0
    droplet = set()

    with open("day18_input.txt", mode="r") as input_file:
        for line in input_file:
            droplet.add(tuple(map(int, line.split(","))))

    min_value = min(min(point) for point in droplet) - 1
    max_value = max(max(point) for point in droplet) + 1

    exterior = [(min_value, min_value, min_value)]
    steam = {exterior[0]}

    while exterior:
        cube = exterior.pop()
        x_coordinate, y_coordinate, z_coordinate = cube
        examined_sides = set()

        if x_coordinate > min_value:
            examined_sides.add((x_coordinate - 1, y_coordinate, z_coordinate))
        if x_coordinate < max_value:
            examined_sides.add((x_coordinate + 1, y_coordinate, z_coordinate))
        if y_coordinate > min_value:
            examined_sides.add((x_coordinate, y_coordinate - 1, z_coordinate))
        if y_coordinate < max_value:
            examined_sides.add((x_coordinate, y_coordinate + 1, z_coordinate))
        if z_coordinate > min_value:
            examined_sides.add((x_coordinate, y_coordinate, z_coordinate - 1))
        if z_coordinate < max_value:
            examined_sides.add((x_coordinate, y_coordinate, z_coordinate + 1))

        for sides in examined_sides - steam:
            if sides in droplet:
                total_area += 1
            else:
                steam.add(sides)
                exterior.append(sides)

    return total_area


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
