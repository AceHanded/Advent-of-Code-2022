"""
Day 15 puzzles of the Advent of Code (15/25).
"""


def silver():
    """The silver star solution."""
    total_vacant_positions = 0
    y_target = 2000000
    grid = []
    ranges = []

    with open("day15_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.strip().split(" ")

            sensor_position = (int(line[2][2:-1]), int(line[3][2:-1]))
            beacon_position = (int(line[-2][2:-1]), int(line[-1][2:]))
            grid.append((sensor_position, beacon_position))

    for sensor, beacon in grid:
        delta = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        y_delta = abs(sensor[1] - y_target)

        if y_delta <= delta:
            x_delta = delta - y_delta
            ranges.append((sensor[0] - x_delta, sensor[0] + x_delta))

    combined_ranges = [sorted(ranges)[0]]

    for range_ in sorted(ranges)[1:]:
        if range_[0] > combined_ranges[-1][1]:
            combined_ranges.append(range_)
        else:
            combined_ranges[-1] = (combined_ranges[-1][0], max([combined_ranges[-1][1], range_[1]]))

    for range_ in combined_ranges:
        total_vacant_positions += range_[1] - range_[0]

    return total_vacant_positions


def gold():
    """The gold star solution."""
    tuning_frequency = 0
    y_max = 4000000
    grid = []

    with open("day15_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.strip().split(" ")

            sensor_position = (int(line[2][2:-1]), int(line[3][2:-1]))
            beacon_position = (int(line[-2][2:-1]), int(line[-1][2:]))
            grid.append((sensor_position, beacon_position))

    for y_coordinate in range(0, y_max):
        ranges = []

        for signal, beacon in grid:
            delta = abs(beacon[0] - signal[0]) + abs(beacon[1] - signal[1])
            y_delta = abs(signal[1] - y_coordinate)

            if y_delta <= delta:
                x_delta = delta - y_delta
                ranges.append((max([signal[0] - x_delta, 0]), min([signal[0] + x_delta, y_max])))

        combined_ranges = [sorted(ranges)[0]]

        for range_ in sorted(ranges)[1:]:
            if range_[0] > combined_ranges[-1][1]:
                combined_ranges.append(range_)
            else:
                combined_ranges[-1] = (combined_ranges[-1][0], max([combined_ranges[-1][1], range_[1]]))

        if len(combined_ranges) > 1 or combined_ranges[0][0] > 0 and combined_ranges[0][1] > y_max:
            if len(combined_ranges) == 1:
                if combined_ranges[0][0] > 0:
                    x_coordinate = 0
                else:
                    x_coordinate = y_max
            else:
                x_coordinate = combined_ranges[0][1] + 1

            tuning_frequency += x_coordinate * y_max + y_coordinate
            break

    return tuning_frequency


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
