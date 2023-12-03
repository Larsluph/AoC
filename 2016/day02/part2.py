UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'
# direction_delta:
#   x: i // 2
#   y: i % 2
direction = (UP, DOWN, LEFT, RIGHT)
deltas = ((0, -1), (0, 1), (-1, 0), (1, 0))
borders = {
    "x": (0, 2),
    "y": (0, 2),
}

digit_mapping = {
    (2, 0): '1',
    (1, 1): '2',
    (2, 1): '3',
    (3, 1): '4',
    (0, 2): '5',
    (1, 2): '6',
    (2, 2): '7',
    (3, 2): '8',
    (4, 2): '9',
    (1, 3): 'A',
    (2, 3): 'B',
    (3, 3): 'C',
    (2, 4): 'D'
}

start = (0, 2)

def calc_distance(a, b = (2, 2)):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

with open('day02\\input.txt') as f:
    data = f.readlines()

final_code = ''
for digit_instruction in data:
    formatted_instruction = digit_instruction.strip()
    for instruction in formatted_instruction:
        index = direction.index(instruction)
        x, y = start
        temp = (x + deltas[index][0], y + deltas[index][1])
        if calc_distance(temp) <= 2:
            start = temp

    # decode digits
    # base pattern:
    # X X 1
    # X 2 3 4
    # 5 6 7 8 9
    # X A B C
    # X X D
    final_code += digit_mapping[start]
    start = (0, 2)

print(final_code)
