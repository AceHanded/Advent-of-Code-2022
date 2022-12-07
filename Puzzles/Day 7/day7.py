"""
Day 7 puzzles of the Advent of Code.
"""


def silver():
    """The silver star solution."""
    total_sizes = 0
    directories = {}
    current_directory = []

    with open("day7_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            split_line = line.split()

            if len(split_line) == 3:
                name = split_line[2]

                if name == "..":
                    current_directory.pop(-1)
                else:
                    current_directory.append(name)

            else:
                if split_line[0] != "$" and split_line[0] != "dir":
                    value = split_line[0]

                    joined_directories = join_directories(current_directory)

                    for directory in joined_directories:
                        if directory not in directories:
                            directories[directory] = 0

                        directories[directory] += int(value)

        for key in directories:
            if directories[key] <= 100000:
                total_sizes += directories[key]

        return total_sizes


def gold():
    """The gold star solution."""
    deleted_directory_size = 0
    directories = {}
    current_directory = []

    with open("day7_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            split_line = line.split()

            if len(split_line) == 3:
                name = split_line[2]

                if name == "..":
                    current_directory.pop(-1)
                else:
                    current_directory.append(name)

            else:
                if split_line[0] != "$" and split_line[0] != "dir":
                    value = split_line[0]

                    joined_directories = join_directories(current_directory)

                    for directory in joined_directories:
                        if directory not in directories:
                            directories[directory] = 0

                        directories[directory] += int(value)

        space_available = 70000000 - directories['/']
        space_required = 30000000 - space_available

        for key in directories:
            if directories[key] > space_required:
                if deleted_directory_size == 0 or deleted_directory_size > directories[key]:
                    deleted_directory_size = directories[key]

        return deleted_directory_size


def join_directories(current_directory):
    """Creates a set of directories, where each subsequent directory contains the previous directories."""
    joined_directories = [''.join(current_directory[:index + 1]) for index in range(0, len(current_directory))]

    return joined_directories


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
