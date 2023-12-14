from itertools import cycle

def process_data(file):
    nodes = list()
    edges = list()
    with open(file) as f:
        for row in f:
            row = row.strip()
            if set(row) == {"R", "L"}:
                instructions = row.strip()
            elif row == "":
                pass
            else:
                row = row.split(" = ")
                nodes.append(row[0])
                edges.append(tuple(row[1].strip("() ").split(", ")))
    return instructions, dict(zip(nodes, edges))


def task_one():
    instructions, network = process_data("input.txt")
    node = "AAA"
    for steps, direction in enumerate(cycle(instructions)):
        if node == "ZZZ":
            print(steps)
            break
        if direction == "L":
            node = network[node][0]
        elif direction == "R":
            node = network[node][1]

def task_two():
    instructions, network = process_data("input.txt")
    start_nodes = [_ for _ in network.keys() if _[-1] == "A"]
    nodes = start_nodes.copy()
    max_matches = 0
    min_matches = 1
    len_instructions = len(instructions)
    z_states = [0 for _ in start_nodes]
    # print(len_instructions, start_nodes)
    for steps, direction in enumerate(cycle(instructions)):
        matches = [_[-1] == "Z" for _ in nodes]
        if sum(matches) > max_matches:
            max_matches = sum(matches)
        if all(matches):
            print(steps)
            break
        elif any(matches):
            z_states = [sum(x) for x in zip(z_states, matches)]
            print(steps, steps/len_instructions, nodes, sum(matches), max_matches, z_states)
            if min(z_states) == 2:
                break

        # elif sum(matches) >= min_matches or steps == 17873:
        #     print(steps, nodes, sum(matches), max_matches)
        #     min_matches += 1
        for i, node in enumerate(nodes):
            # if i % 6 == 0 and node in start_nodes:
            #     print(steps, nodes, sum(matches), max_matches)
            if direction == "L":
                nodes[i] = network[node][0]
            elif direction == "R":
                nodes[i] = network[node][1]

task_two()