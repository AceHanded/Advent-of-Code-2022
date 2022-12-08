"""
Day 8 puzzles of the Advent of Code.
"""


def silver():
    """The silver star solution."""
    tree_rows = []

    with open("day8_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()
            tree_rows.append(line)

        trees_visible = 2 * len(tree_rows[0]) + 2 * (len(tree_rows) - 2)

        for row_number, row in enumerate(tree_rows[1:-1], 1):
            for column_number, column_value in enumerate(row[1:-1], 1):
                value = row[column_number]

                taller_left = [visibility < value for visibility in reversed(row[:column_number])]
                taller_right = [visibility < value for visibility in row[column_number + 1:]]
                taller_up = [visibility < value for visibility in (line[column_number] for line in
                                                                   reversed(tree_rows[:row_number]))]
                taller_down = [visibility < value for visibility in (line[column_number] for line in
                                                                     tree_rows[row_number + 1:])]

                if all(taller_left) or all(taller_right) or all(taller_up) or all(taller_down):
                    trees_visible += 1

    return trees_visible


def gold():
    """The gold star solution."""
    highest_scenic_score = 0
    tree_rows = []

    with open("day8_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.rstrip()
            tree_rows.append(line)

        for row_number, row in enumerate(tree_rows[1:-1], 1):
            for column_number, column_value in enumerate(row[1:-1], 1):
                value = row[column_number]

                taller_left = [visibility < value for visibility in reversed(row[:column_number])]
                taller_right = [visibility < value for visibility in row[column_number + 1:]]
                taller_up = [visibility < value for visibility in (line[column_number] for line in
                                                                   reversed(tree_rows[:row_number]))]
                taller_down = [visibility < value for visibility in (line[column_number] for line in
                                                                     tree_rows[row_number + 1:])]

                vd_left = calculate_view_distance(taller_left)
                vd_right = calculate_view_distance(taller_right)
                vd_up = calculate_view_distance(taller_up)
                vd_down = calculate_view_distance(taller_down)

                highest_scenic_score = max(highest_scenic_score, vd_left * vd_right * vd_up * vd_down)

    return highest_scenic_score


def calculate_view_distance(taller_trees):
    """Calculates the view distance of a tree in any one direction."""
    try:
        view_distance = taller_trees.index(False) + 1

        return view_distance

    except ValueError:
        view_distance = len(taller_trees)

        return view_distance


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
