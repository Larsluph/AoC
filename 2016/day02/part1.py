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

start = (1, 1)

with open('day02\\input.txt') as f:
    data = f.readlines()

final_code = ''
for digit_instruction in data:
    formatted_instruction = digit_instruction.strip()
    for instruction in formatted_instruction:
        index = direction.index(instruction)
        x, y = start
        start = (max(min(x + deltas[index][0], borders['x'][1]), borders['x'][0]),
                 max(min(y + deltas[index][1], borders['y'][1]), borders['y'][0]))

        # decode digits
        decoded_digit = start[0] + 1 + start[1] * 3
    final_code += str(decoded_digit)
    start = (0, 0)

print(final_code)
