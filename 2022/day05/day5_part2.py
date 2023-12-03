import re

pinstruction = re.compile(r'move (?P<length>\d+) from (?P<stack_a>\d) to (?P<stack_b>\d)')

# read input
with open('input.txt', 'r') as f:
    init_stack = list()
    while (line := f.readline()) != '\n':
        init_stack.append(line)
    # indexes = list(filter(lambda x: x != ' ', init_stack.pop()))
    indexes = len([x for x in init_stack.pop()[:-1] if x != ' '])
    instructions = f.readlines()

# format stacks
stacks = list()
for x in range(indexes):
    stack = list()
    for i in range(len(init_stack)):
        box = init_stack[i][x*4 + 1]
        if box != ' ':
            stack.insert(0, box)
    stacks.append(stack)

# execute instructions
for instruction in instructions:
    groups = pinstruction.match(instruction).groupdict()
    length = int(groups["length"])
    stack_a = stacks[int(groups["stack_a"])-1]
    stack_b = stacks[int(groups["stack_b"])-1]
    temp = list()
    for i in range(length):
        temp.append(stack_a.pop())
    for i in range(length):
        stack_b.append(temp.pop())

# get output
top_boxes = str()
for stack in stacks:
    top_boxes += stack.pop()
print(''.join(top_boxes))
