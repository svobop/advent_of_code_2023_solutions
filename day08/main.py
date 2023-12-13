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


task_one()