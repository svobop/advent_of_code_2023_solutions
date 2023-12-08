test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

with open("input.txt") as f:
    data = f.read()

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
            games_column.append([[int(_) for _ in winning_numbers], [int(_) for _ in draw_numbers]])
    return dict(zip(labels_column, games_column))


def test_case():
    data = process_data(test_data)
    total_points = score_points(data)
    print(total_points)
    return total_points == 13


def test_case2():
    data = process_data(test_data)
    total_cards = duplicate_cards(data)
    print(total_cards)
    return total_cards == 30

def score_points(data):
    total_points = 0
    for game, numbers in data.items():
        match_count = 0
        for draw_number in numbers[1]:
            if draw_number in numbers[0]:
                match_count += 1
        card_points = 0 if match_count == 0 else 2 ** (match_count - 1)
        total_points += card_points
    return total_points

def duplicate_cards(data):
    number_of_copies = dict()
    for game, numbers in data.items():
        copies_of_current_card = number_of_copies.get(game, 1)
        match_count = 0
        for draw_number in numbers[1]:
            if draw_number in numbers[0]:
                match_count += 1
        game_number = int(game.split()[1])
        for i in range(game_number, game_number + match_count+1):
            game_ = "Card " + str(i).rjust(3, ' ')
            if number_of_copies.get(game_) and i != game_number:
                number_of_copies[game_] += copies_of_current_card
            elif i == game_number:
                number_of_copies[game_] = copies_of_current_card
            else:
                number_of_copies[game_] = 1 + copies_of_current_card

        # print(game)
        # print(list(range(game_number, game_number + match_count+1)))
        # print(number_of_copies)
    return sum(number_of_copies.values())

if __name__ == '__main__':
    if test_case():
        print("test passed")
    else:
        print("test failed")
    if test_case2():
        print("test passed")
    else:
        print("test failed")
    print(score_points(process_data(data)))
    print(duplicate_cards(process_data(data)))