"""
Day 13 puzzles of the Advent of Code (13/25).
"""


def silver():
    """The silver star solution."""
    lines = []
    packets = []
    index = 0
    total_indices = 0

    with open("day13_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.strip()

            lines.append(line)

    for line in lines:
        if line == "":
            continue

        packets.append(eval(line))

    while index < len(packets) - 1:
        in_correct_order = compare_packets(packets[index], packets[index + 1])

        if in_correct_order:
            total_indices += index // 2 + 1

        index += 2

    return total_indices


def gold():
    """The gold star solution."""
    lines = []
    packets = []
    decoder_key = 0

    with open("day13_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.strip()

            lines.append(line)

    for line in lines:
        if line == "":
            continue

        packets.append(eval(line))

    packets.append([[2]]), packets.append([[6]])

    for index in range(len(packets)):
        for index2 in range(index + 1, len(packets)):
            in_correct_order = compare_packets(packets[index], packets[index2])

            if not in_correct_order:
                packets[index], packets[index2] = packets[index2], packets[index]

    decoder_key += (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

    return decoder_key


def compare_packets(left, right):
    """Compares whether or not the provided packets are in the correct order."""
    index = 0

    while True:
        if len(left) <= index < len(right):
            return True
        elif len(right) <= index < len(left):
            return False
        elif index >= len(left) and index >= len(right):
            return None

        if isinstance(left[index], int) and isinstance(right[index], int):
            if left[index] < right[index]:
                return True
            elif right[index] < left[index]:
                return False
        elif isinstance(left[index], list) and isinstance(right[index], list):
            result = compare_packets(left[index], right[index])

            if result is not None:
                return result
        elif isinstance(left[index], list) and isinstance(right[index], int):
            result = compare_packets(left[index], [right[index]])

            if result is not None:
                return result
        elif isinstance(left[index], int) and isinstance(right[index], list):
            result = compare_packets([left[index]], right[index])

            if result is not None:
                return result

        index += 1


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
