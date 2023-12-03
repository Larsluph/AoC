import numpy as np

with open('input.txt', 'r') as f:
    tree_map = np.array([[int(char) for char in line.strip()] for line in f.readlines()])
check_map = np.zeros(tree_map.shape, dtype=np.bool8)

def check_up_down():
    for y in range(tree_map.shape[1]):
        last_height = -1
        for x in range(tree_map.shape[0]):
            height = tree_map[x,y]
            # print(x, y, height)
            if height > last_height:
                check_map[x, y] = True
                last_height = height

def check_down_up():
    for y in range(tree_map.shape[1]):
        last_height = -1
        for x in range(tree_map.shape[0]):
            height = tree_map[-(x+1), y]
            # print(-(x+1), y, height)
            if height > last_height:
                check_map[-(x+1), y] = True
                last_height = height

def check_left_right():
    for x in range(tree_map.shape[0]):
        last_height = -1
        for y in range(tree_map.shape[1]):
            height = tree_map[x, y]
            # print(x, y, height)
            if height > last_height:
                check_map[x, y] = True
                last_height = height

def check_right_left():
    for x in range(tree_map.shape[0]):
        last_height = -1
        for y in range(tree_map.shape[1]):
            height = tree_map[x, -(y+1)]
            # print(x, -(y+1), height)
            if height > last_height:
                check_map[x, -(y+1)] = True
                last_height = height

def get_result():
    total_sum = 0
    for row in check_map:
        for check in row:
            total_sum += check
    return total_sum

print("up->down")
check_up_down()
print("up<-down")
check_down_up()
print("left->right")
check_left_right()
print("left<-right")
check_right_left()

# print(check_map)

print(get_result())
