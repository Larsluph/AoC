"""
DAY 1 - PART 1
"""

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

def parse_line(line):
    # forward
    for char in line:
        if char.isdigit():
            start = char
            break
    # backward
    for char in line[::-1]:
        if char.isdigit():
            end = char
            break

    return start, end

calibration_values = map(parse_line, lines)
formatted_values = map(lambda x: int(''.join(x)), calibration_values)
print(sum(formatted_values))
