"""
Day 19 puzzles of the Advent of Code (19/25).
"""


import numpy


COST_ARRAY = lambda *values: numpy.array(values)
KEY_CHECK = lambda a: tuple(sum(a))


def silver():
    """The silver star solution."""
    quality_level = 0
    minutes = 24
    blueprints = []

    with open("day19_input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip().split()

            index, ore, ore2, ore3, clay, ore4, obsidian = (int(line[1][:-1]), int(line[6]), int(line[12]),
                                                            int(line[18]), int(line[21]), int(line[27]), int(line[30]))

            blueprints.append((index, (COST_ARRAY(0, 0, 0, ore), COST_ARRAY(0, 0, 0, 1)),
                                      (COST_ARRAY(0, 0, 0, ore2), COST_ARRAY(0, 0, 1, 0)),
                                      (COST_ARRAY(0, 0, clay, ore3), COST_ARRAY(0, 1, 0, 0)),
                                      (COST_ARRAY(0, obsidian, 0, ore4), COST_ARRAY(1, 0, 0, 0)),
                                      (COST_ARRAY(0, 0, 0, 0), COST_ARRAY(0, 0, 0, 0))))

    for index, *blueprint in blueprints:
        geode_production = [(COST_ARRAY(0, 0, 0, 0), COST_ARRAY(0, 0, 0, 1))]

        for _ in range(minutes):
            geodes = list()

            for owned, required in geode_production:
                for cost, production in blueprint:
                    if all(owned >= cost):
                        geodes.append((owned + required - cost, required + production))

            geode_production = sorted(geodes, key=KEY_CHECK)[-1000:]

        quality_level += max(geode_production, key=KEY_CHECK)[0][0] * index

    return quality_level


def gold():
    """The gold star solution."""
    total_geodes = 1
    minutes = 32
    blueprints = []

    with open("day19_input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip().split()

            index, ore, ore2, ore3, clay, ore4, obsidian = (int(line[1][:-1]), int(line[6]), int(line[12]),
                                                            int(line[18]), int(line[21]), int(line[27]), int(line[30]))

            blueprints.append((index, (COST_ARRAY(0, 0, 0, ore), COST_ARRAY(0, 0, 0, 1)),
                                      (COST_ARRAY(0, 0, 0, ore2), COST_ARRAY(0, 0, 1, 0)),
                                      (COST_ARRAY(0, 0, clay, ore3), COST_ARRAY(0, 1, 0, 0)),
                                      (COST_ARRAY(0, obsidian, 0, ore4), COST_ARRAY(1, 0, 0, 0)),
                                      (COST_ARRAY(0, 0, 0, 0), COST_ARRAY(0, 0, 0, 0))))

    for index, *blueprint in blueprints:
        geode_production = [(COST_ARRAY(0, 0, 0, 0), COST_ARRAY(0, 0, 0, 1))]

        for _ in range(minutes):
            geodes = list()

            for owned, required in geode_production:
                for cost, production in blueprint:
                    if all(owned >= cost):
                        geodes.append((owned + required - cost, required + production))

            geode_production = sorted(geodes, key=KEY_CHECK)[-5000:]

        if index < 4:
            total_geodes *= max(geode_production, key=KEY_CHECK)[0][0]

    return total_geodes


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
