test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def process_data(data):
    data = data.split("\n")
    labels_column = list()
    games_column = list()
    for row in data:
        if row != "":
            row = row.split(":")
            label = row[0]
            labels_column.append(label)
            games = row[1]
            games = games.split("|")
            winning_numbers = games[0].split()
            draw_numbers = games[1].split()
            games_column.append([[int(_) for _ in winning_numbers], [_.strip() for _ in draw_numbers]])
    return dict(zip(labels_column, games_column))


print(process_data(test_data))

print()
