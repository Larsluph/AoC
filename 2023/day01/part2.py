"""
DAY 1 - PART 2
"""

import re

translate_table = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

pattern = re.compile(r"^.*?(\d).*(\d).*?$")

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

    print(line, start, end)

    return start, end

def apply_translation(line):
    for k, v in translate_table.items():
        line = line.replace(k, v)
    return line

formatted_lines = map(apply_translation, lines)
calibration_values = map(parse_line, formatted_lines)
formatted_values = map(lambda x: int(''.join(x)), calibration_values)
print(sum(formatted_values))
