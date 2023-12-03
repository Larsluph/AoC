with open(r'day01\input.txt', 'r') as f:
    instructions = f.read().strip().split(', ')

# current coordinates of our current position
current_x, current_y = 0, 0

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

    if direction == NORTH:
        current_y += amount
    elif direction == SOUTH:
        current_y -= amount
    elif direction == WEST:
        current_x -= amount
    elif direction == EAST:
        current_x += amount

# Compute taxicab distance
print(abs(current_x) + abs(current_y))
