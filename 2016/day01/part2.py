def disp_answer(x, y):
    # Compute taxicab distance
    print(abs(x) + abs(y))


with open(r'day01\input.txt', 'r') as f:
    instructions = f.read().strip().split(', ')

# current coordinates of our current position
current_x, current_y = 0, 0

# we store current coordinates to know when we visit a single location twice
position_history = set()

# current orientation of our cursor
# 0 for North, 1 for East, 2 for South and 4 for West
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

direction = NORTH
for instruction in instructions:
    turn = instruction[0]
    amount = int(instruction[1:])

    if turn == 'L':
        direction -= 1
    elif turn == 'R':
        direction += 1
    else:
        raise NotImplementedError

    # don't overflow direction
    direction %= 4

    for step in range(amount):
        if direction == NORTH:
            current_y += 1
        elif direction == SOUTH:
            current_y -= 1
        elif direction == WEST:
            current_x -= 1
        elif direction == EAST:
            current_x += 1

        if (current_x, current_y) in position_history:
            disp_answer(current_x, current_y)
            exit()
        position_history.add((current_x, current_y))
