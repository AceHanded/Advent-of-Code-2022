"""
Day 4 puzzles of the Advent of Code (4/25).
"""


def silver():
    """The silver star solution."""
    total_overlaps = 0

    with open("day4_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            elf, elf2 = line.split(",")
            elf_sect, elf_sect2 = elf.split("-")
            elf2_sect, elf2_sect2 = elf2.split("-")

            elf_sects = [section for section in range(int(elf_sect), int(elf_sect2) + 1)]
            elf2_sects = [section for section in range(int(elf2_sect), int(elf2_sect2) + 1)]

            if all(sect in elf_sects for sect in elf2_sects) or all(sect in elf2_sects for sect in elf_sects):
                total_overlaps += 1

    return total_overlaps


def gold():
    """The gold star solution."""
    total_overlaps = 0

    with open("day4_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()

            elf, elf2 = line.split(",")
            elf_sect, elf_sect2 = elf.split("-")
            elf2_sect, elf2_sect2 = elf2.split("-")

            elf_sects = [section for section in range(int(elf_sect), int(elf_sect2) + 1)]
            elf2_sects = [section for section in range(int(elf2_sect), int(elf2_sect2) + 1)]

            if any(sect in elf_sects for sect in elf2_sects):
                total_overlaps += 1

    return total_overlaps


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
