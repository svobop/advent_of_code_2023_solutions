def process_data(file):
    hands = list()
    with open(file) as f:
        for row in f:
            row = row.split()
            hands.append([row[0], int(row[1])])
    return hands

CARD_VALUE = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13
}
def card_value(card):
    return CARD_VALUE[card]


def is_five_of_a_kind(hand):
    if len(set(hand)) == 1:
        return True
    else:
        return False


def hand_histogram(hand):
    hist = dict()
    for card in set(hand):
        hist[card] = list(hand).count(card)
    return hist


def is_four_of_a_kind(hand):
    hist = hand_histogram(hand)
    if {4, 1} == set(hist.values()):
        return True
    else:
        return False


def is_full_house(hand):
    hist = hand_histogram(hand)
    if {3, 2} == set(hist.values()):
        return True
    else:
        return False


def is_three_of_a_kind(hand):
    hist = hand_histogram(hand)
    if {3, 1} == set(hist.values()):
        return True
    else:
        return False


def is_two_pair(hand):
    hist = hand_histogram(hand)
    if [1, 2, 2] == sorted(hist.values()):
        return True
    else:
        return False


def is_one_pair(hand):
    hist = hand_histogram(hand)
    if [1, 1, 1, 2] == sorted(hist.values()):
        return True
    else:
        return False


def is_high_card(hand):
    hist = hand_histogram(hand)
    if {1} == set(hist.values()):
        return True
    else:
        return False


def hand_value(hand):
    card_value_string = "".join([str(card_value(_)).zfill(2) for _ in list(hand)])
    if is_five_of_a_kind(hand):
        return "1" + card_value_string
    elif is_four_of_a_kind(hand):
        return "2" + card_value_string
    elif is_full_house(hand):
        return "3" + card_value_string
    elif is_three_of_a_kind(hand):
        return "4" + card_value_string
    elif is_two_pair(hand):
        return "5" + card_value_string
    elif is_one_pair(hand):
        return "6" + card_value_string
    elif is_high_card(hand):
        return "7" + card_value_string


def task_one(input):
    total = 0
    i = 1
    for hand, bid in sorted(process_data(input), key=lambda x: hand_value(x[0]), reverse=True):
        # print(hand, i, bid)
        total += i * bid
        i += 1
    print(total)


task_one("input.txt")

