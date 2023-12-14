def process_data(file):
    sequences = list()
    with open(file) as f:
        for row in f:
            row = row.strip()
            if row == "":
                pass
            else:
                row = row.split(" ")
                sequences.append([int(_) for _ in row])
    return sequences


def get_dif_sequence(sequence):
    return [pair[1] - pair[0] for pair in zip(sequence[:], sequence[1:])]


def predict_next_number(sequence):
    dif_sequences = [sequence]
    dif_sequence = sequence
    while any([_ != 0 for _ in dif_sequence]):
        dif_sequence = get_dif_sequence(dif_sequence)
        dif_sequences.append(dif_sequence)
    dif_sequences.reverse()
    last_number = 0
    for dif_sequence in dif_sequences:
        dif_sequence.append(dif_sequence[-1] + last_number)
        last_number = dif_sequence[-1]
    return dif_sequences[-1][-1]


def task_one(input):
    sequences = process_data(input)
    next_numbers = list()
    for sequence in sequences:
        next_number = predict_next_number(sequence)
        next_numbers.append(next_number)
    print(sum(next_numbers))


task_one("input.txt")