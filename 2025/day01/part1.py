import re

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

pattern = re.compile(r'^(L|R)(\d+)$')

count = 0
pos = 50
for line in lines:
    match = re.match(pattern, line)
    if match is None:
        print("No match found:", line)
        continue

    direction, raw_amount = match.groups()

    amount = int(raw_amount)

    match direction:
        case 'L':
            pos -= amount
        case 'R':
            pos += amount
        case _:
            print("aaaaaaaaaaa")

    pos %= 100

    if pos == 0:
        count += 1

print(count)
