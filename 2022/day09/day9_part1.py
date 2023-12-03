UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

prev_head_pos = [0, 0]
head_pos = [0, 0]
tail_pos = [0, 0]
map_tail_pos = set()

def tail_oor():
    return head_pos[0] > tail_pos[0]+1 or head_pos[0] < tail_pos[0]-1 \
        or head_pos[1] > tail_pos[1]+1 or head_pos[1] < tail_pos[1]-1

with open('input.txt', 'r') as f:
    instructions = list(map(lambda line: line.strip().split(' '), f.readlines()))

for instruction in instructions:
    ins = instruction[0]
    value = int(instruction[1])
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

        # tail movement
        if tail_oor():
            tail_pos = prev_head_pos

        # processing for result
        map_tail_pos.add(tuple(tail_pos))
        # print(tail_pos, head_pos)

# print(map_tail_pos)
print(len(map_tail_pos))
