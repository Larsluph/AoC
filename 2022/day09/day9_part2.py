UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

def tail_oor(head, tail):
    return head[0] > tail[0]+1 or head[0] < tail[0]-1 \
        or head[1] > tail[1]+1 or head[1] < tail[1]-1

def get_delta(before, after):
    return (after[0] - before[0],
            after[1] - before[1])

def merge_delta(data, delta):
    data[0] += delta[0]
    data[1] += delta[1]

def debug_state():
    # detect min and max
    min_val = head_pos.copy()
    max_val = head_pos.copy()
    for state in tail_pos:
        if state[0] > max_val[0]:
            max_val[0] = state[0]
        if state[0] < min_val[0]:
            min_val[0] = state[0]
        if state[1] > max_val[1]:
            max_val[1] = state[1]
        if state[1] < min_val[1]:
            min_val[1] = state[1]

    # normalize min values (can't be negative in indexes)
    # fix applied: set min values to (0, 0) so all values are positive
    normalized_values = (-min_val[0], -min_val[1])

    # generate grid
    debug_map = [["." for _ in range(min_val[0], max_val[0]+1)] for _ in range(min_val[1], max_val[1]+1)]
    for i, knot in enumerate((*tail_pos[::-1], head_pos)):
        debug_map[knot[1]+normalized_values[1]][knot[0]+normalized_values[0]] = str(9-i) if i < 9 else "H"

    # display
    for line in debug_map:
        print("".join(line))

with open('input.txt', 'r') as f:
    instructions = list(map(lambda line: line.strip().split(' '), f.readlines()))

head_pos = [0, 0]
tail_pos = [[0, 0] for _ in range(9)]
map_tail_pos = set()

for instruction in instructions:
    ins = instruction[0]
    value = int(instruction[1])
    # print("===", ins, value, "===")
    for i in range(value):
        # head movement
        prev_head_pos = head_pos.copy()
        if ins == UP:
            head_pos[1] -= 1
        elif ins == DOWN:
            head_pos[1] += 1
        elif ins == LEFT:
            head_pos[0] -= 1
        elif ins == RIGHT:
            head_pos[0] += 1

        # tails movement
        delta = None
        prev_tail_before_move = prev_head_pos.copy()
        prev_tail_after_move = head_pos.copy()
        for i, tail in enumerate(tail_pos):
            tail_before_move = tail.copy()
            if tail_oor(prev_tail_after_move, tail_before_move):
                tmp_delta = get_delta(tail_before_move, prev_tail_after_move)
                final_delta = min(max(tmp_delta[0], -1), 1), min(max(tmp_delta[1], -1), 1)
                tail[0] += final_delta[0]
                tail[1] += final_delta[1]
            else:
                delta = None
            prev_tail_before_move = tail_before_move.copy()
            prev_tail_after_move = tail.copy()
        # print(head_pos, tail_pos)
        # debug_state()

        # processing for result
        map_tail_pos.add(tuple(tail_pos[-1]))
        # print("=====")

# print(map_tail_pos)
print(len(map_tail_pos))
