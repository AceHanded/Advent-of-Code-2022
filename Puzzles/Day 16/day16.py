"""
Day 16 puzzles of the Advent of Code (16/25).
"""


import heapq


def silver():
    """The silver star solution."""
    highest_pressure = 0
    start_valve = "AA"
    flow_rates = {}
    connections = {}

    with open("day16_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.strip().split()

            name, flow_rate, connected_valves = line[1], int(line[4][5:-1]), "".join(line[9:]).split(",")

            flow_rates[name] = flow_rate
            connections[name] = connected_valves

    for name, connected_valves in list(connections.items()):
        del connections[name]
        connections[name] = {connected_valve: 1 for connected_valve in connected_valves}

    distances = {name: find_paths(connections, name) for name in connections if name == start_valve or flow_rates[name]}
    valves_with_flow = {valve for valve in flow_rates if flow_rates[valve]}

    for name, valve_distances in distances.items():
        distances[name] = {valve: connections for valve, connections in valve_distances.items() if flow_rates[valve]}

    orders = all_orders(distances, start_valve, valves_with_flow, [], 30)

    highest_pressure += max(run_order(distances, flow_rates, start_valve, order, 30) for order in orders)

    return highest_pressure


def gold():
    """The gold star solution."""
    highest_pressure = 0
    start_valve = "AA"
    flow_rates = {}
    connections = {}

    with open("day16_input.txt", mode="r") as input_file:
        for line in input_file:
            line = line.strip().split()

            name, flow_rate, connected_valves = line[1], int(line[4][5:-1]), "".join(line[9:]).split(",")

            flow_rates[name] = flow_rate
            connections[name] = connected_valves

    for name, connected_valves in list(connections.items()):
        del connections[name]
        connections[name] = {connected_valve: 1 for connected_valve in connected_valves}

    distances = {name: find_paths(connections, name) for name in connections if name == start_valve or flow_rates[name]}
    valves_with_flow = {valve for valve in flow_rates if flow_rates[valve]}

    for name, valve_distances in distances.items():
        distances[name] = {valve: connections for valve, connections in valve_distances.items() if flow_rates[valve]}

    orders = all_orders(distances, start_valve, valves_with_flow, [], 30)
    scores = [(run_order(distances, flow_rates, start_valve, order, 26), set(order)) for order in orders]
    scores.sort(key=lambda x: -x[0])

    for index, (scores_score, scores_orders) in enumerate(scores):
        if scores_score * 2 < highest_pressure:
            break

        for scores_score2, scores_orders2 in scores[index + 1:]:
            if not scores_orders & scores_orders2:
                score = scores_score + scores_score2

                if score > highest_pressure:
                    highest_pressure = score

    return highest_pressure


def find_paths(connections, goal):
    """Finds the lengths of the paths between valves."""
    queue = [(0, goal)]
    path_lengths = {goal: 0}

    while queue:
        distance, current_valve = heapq.heappop(queue)

        for valve, valve_distance in connections[current_valve].items():
            if valve not in path_lengths or distance + valve_distance < path_lengths[valve]:
                path_lengths[valve] = distance + valve_distance
                heapq.heappush(queue, (distance + valve_distance, valve))

    return path_lengths


def all_orders(distances, valve, queue, finished, minutes):
    """Finds and yields all valve orders."""
    for next_valve in queue:
        distance = distances[valve][next_valve] + 1

        if distance < minutes:
            yield from all_orders(distances, next_valve, queue - {next_valve},
                                  finished + [next_valve], minutes - distance)

    yield finished


def run_order(distances, flow_rates, start_valve, valves, minutes):
    """Calculates the amount of pressure released."""
    pressure_release = 0
    current_valve = start_valve

    for valve in valves:
        distance = distances[current_valve][valve] + 1
        minutes -= distance
        pressure_release += minutes * flow_rates[valve]
        current_valve = valve

    return pressure_release


def main():
    silver_ = silver()
    gold_ = gold()
    print(f"Silver: {silver_}\nGold: {gold_}")


if __name__ == "__main__":
    main()
