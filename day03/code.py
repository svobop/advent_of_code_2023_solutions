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

def get_numbers(data):
    numbers = []
    for i, row in enumerate(split_into_rows(data)):
        for match in re.finditer(r"(\d+)", row):
            numbers.append({"number": match.group(), "span": tuple([i]) + match.span()})
    return numbers

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
            print(i, j, data[i][j])
            if data[i][j] not in ".0123456789":
                return True
    return False



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

def main():
    total = 0
    for number in get_numbers(data):
        adjencent = check_adjecent_symbol(data, number["span"])
        print(number, adjencent)
        if adjencent:
            total += int(number["number"])
    print(f"total: {total}")

#print(len(split_into_rows(data)))

main()


