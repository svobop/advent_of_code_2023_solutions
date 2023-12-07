import re

with open("input.txt") as f:
    data = f.read()
    data = data.rstrip()

test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def split_into_rows(data):
    return data.split("\n")

def get_matches(data, re_pattern):
    matches = []
    for i, row in enumerate(split_into_rows(data)):
        for match in re.finditer(re_pattern, row):
            matches.append({"match": match.group(), "span": tuple([i]) + match.span()})
    return matches

def check_adjecent_symbol(data, span):
    data = split_into_rows(data)
    row_lenght = len(data[0])
    column_lenght = len(data)
    print(row_lenght, column_lenght)
    horizontal_range = range(
        span[1]-1 if span[1]-1 >= 0 else 0,
        span[2]+1 if span[2]+1 <= row_lenght else row_lenght
        )
    vertical_range = range(
        span[0]-1 if span[0]-1 >= 0 else 0,
        span[0]+2 if span[0]+2 <= column_lenght else column_lenght
        )
    print(horizontal_range, vertical_range)
    for i in vertical_range:
        for j in horizontal_range:
            if i != span[0] or ( i == span[0] and (j == span[1]-1 or j == span[2])):
                print(i, j, data[i][j])
                if data[i][j] not in ".0123456789":
                    return True
    return False

def check_adjecent_numbers(data, numbers, span):
    output = set()
    data = split_into_rows(data)
    row_lenght = len(data[0])
    column_lenght = len(data)
    print(row_lenght, column_lenght)
    horizontal_range = range(
        span[1]-1 if span[1]-1 >= 0 else 0,
        span[2]+1 if span[2]+1 <= row_lenght else row_lenght
        )
    vertical_range = range(
        span[0]-1 if span[0]-1 >= 0 else 0,
        span[0]+2 if span[0]+2 <= column_lenght else column_lenght
        )
    print(horizontal_range, vertical_range)
    for i in vertical_range:
        row_numbers = [_ for _ in numbers if _["span"][0] == i]
        for j in horizontal_range:
            if i != span[0] or ( i == span[0] and (j == span[1]-1 or j == span[2])):
                print(i, j, data[i][j])
                output = output.union({ _["match"] for _ in row_numbers if _["span"][1]-1 < j and j < _["span"][2] })
    return list(output)



def test_case_1():
    total = 0
    for number in get_numbers(test_data):
        adjencent = check_adjecent_symbol(test_data, number["span"])
        print(number, adjencent)
        if adjencent:
            total += int(number["number"])
    print(f"total: {total}")
    if total == 4361:
        print("test passed")

def first_task():
    total = 0
    for number in get_matches(data, r"(\d+)"):
        adjencent = check_adjecent_symbol(data, number["span"])
        print(number, adjencent)
        if adjencent:
            total += int(number["match"])
    print(f"total: {total}")

def second_task():
    total = 0
    numbers = get_matches(data, r"(\d+)")
    for symbol in get_matches(data, r"(\*)"):
        adjencent_numbers = check_adjecent_numbers(data, numbers, symbol["span"])
        print(symbol, adjencent_numbers)
        if len(adjencent_numbers) == 2:
            total += int(adjencent_numbers[0])*int(adjencent_numbers[1])
    print(f"total: {total}")


#print(len(split_into_rows(data)))

second_task()


