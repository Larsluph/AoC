"""
DAY 1 - PART 2
"""

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

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

def match_word(line, i) -> str | bool:
    for k, v in translate_table.items():
        if line[i:i+len(k)] == k:
            return v

def parse_line(line):
    # forward
    for i in range(len(line)-1):
        char = line[i]
        if char.isdigit():
            start = char
            break
        elif (digit := match_word(line, i)):
            start = digit
            break
    # backward
    for i in range(len(line)-2, -1, -1):
        char = line[i]
        if char.isdigit():
            end = char
            break
        elif (digit := match_word(line, i)):
            end = digit
            break

    print(line, start, end)

    return start + end

calibration_values = map(parse_line, lines)
formatted_values = map(int, calibration_values)
print(sum(formatted_values))
