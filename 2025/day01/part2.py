import re

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

pattern = re.compile(r'^(L|R)(\d+)$')

count = 0
pos = 50
for i, line in enumerate(lines):
    # print(f"line {i}", end="")
    match = re.match(pattern, line)
    if match is None:
        print("No match found:", line)
        continue

    direction, raw_amount = match.groups()

    amount = int(raw_amount)

    if pos == 0 and direction == 'L':
        # We already counted 0 when stepping on it last iter
        count -= 1

    match direction:
        case 'L':
            pos -= amount
        case 'R':
            pos += amount
        case _:
            print("Unexpected direction:", direction)
            break

    click, pos = divmod(pos, 100)

    count += abs(click)

    if pos == 0 and direction == 'L':
        # We just landed on 0 so counting to add current
        count += 1

    # if click != 0:
    #     print(f"{i:04} | {old_pos=}, {direction=}, {amount=}, {pos=}, {abs(click)=}, {count=}")

print(count)
