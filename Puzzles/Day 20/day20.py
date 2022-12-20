"""
Day 20 puzzles of the Advent of Code (20/25).
"""


def silver():
    """The silver star solution."""
    coordinate_sum = 0
    index = 0
    encryption = []

    with open("day20_input.txt", "r") as input_file:
        for index, line in enumerate(input_file):
            encryption.append((index, int(line.strip())))

    for encryption_id, value in encryption[:]:
        for index in range(len(encryption)):
            if encryption[index][0] == encryption_id:
                break

        for _ in range(abs(value)):
            new_index = (index + (value // abs(value))) % len(encryption)
            encryption[index], encryption[new_index] = encryption[new_index], encryption[index]
            index = new_index

    for index in range(len(encryption)):
        if encryption[index][1] == 0:
            break

    coordinate_sum += (encryption[(index + 1000) % len(encryption)][1] + encryption[(index + 2000) % len(encryption)][1]
                       + encryption[(index + 3000) % len(encryption)][1])

    return coordinate_sum


def gold():
    """The gold star solution."""
    coordinate_sum = 0
    decryption_key = 811589153
    index = 0
    encryption = []

    with open("day20_input.txt", "r") as input_file:
        for index, line in enumerate(input_file):
            encryption.append((index, int(line.strip())))

    order = encryption[:]
    encryption = [(encryption_id, decryption_key * value) for (encryption_id, value) in order]

    for count in range(10):
        for encryption_id, value in order:
            for index in range(len(encryption)):
                if encryption[index][0] == encryption_id:
                    break

            mixes = encryption[index][1] % (len(encryption) - 1)

            for _ in range(abs(mixes)):
                new_index = (index + (mixes // abs(mixes))) % len(encryption)
                encryption[index], encryption[new_index] = encryption[new_index], encryption[index]
                index = new_index

    for index in range(len(encryption)):
        if encryption[index][1] == 0:
            break

    coordinate_sum += (encryption[(index + 1000) % len(encryption)][1] + encryption[(index + 2000) % len(encryption)][1]
                       + encryption[(index + 3000) % len(encryption)][1])

    return coordinate_sum


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
