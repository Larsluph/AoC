import numpy as np

with open('input.txt', 'r') as f:
    tree_map = np.array([[int(char) for char in line.strip()] for line in f.readlines()])
check_map = np.zeros(tree_map.shape, dtype=np.uint32)

def traverse_left(x, y):
    base = tree_map[y,x]
    weight = 0
    for i in range(x-1, -1, -1):
        weight += 1
        if tree_map[y,i] >= base:
            break
    return weight

def traverse_right(x, y):
    base = tree_map[y,x]
    weight = 0
    for i in range(x+1, tree_map.shape[1]):
        weight += 1
        if tree_map[y,i] >= base:
            break
    return weight

def traverse_up(x, y):
    base = tree_map[y,x]
    weight = 0
    for j in range(y-1, -1, -1):
        weight += 1
        if tree_map[j,x] >= base:
            break
    return weight

def traverse_down(x, y):
    base = tree_map[y,x]
    weight = 0
    for j in range(y+1, tree_map.shape[0]):
        weight += 1
        if tree_map[j,x] >= base:
            break
    return weight

def get_result():
    result = 0
    for row in check_map:
        for check in row:
            result = max(result, check)
    return result

for y in range(tree_map.shape[0]):
    for x in range(tree_map.shape[1]):
        final_weight = 1
        final_weight *= traverse_down(x, y)
        final_weight *= traverse_left(x, y)
        final_weight *= traverse_right(x, y)
        final_weight *= traverse_up(x, y)
        check_map[y,x] = final_weight
        # print(f"{x}, {y}: {tree_map[y,x]} ({final_weight})")

print(get_result())
