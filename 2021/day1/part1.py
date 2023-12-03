with open("day1\\input.txt", 'r') as f:
    depths = f.readlines()

prev_depth = int(depths[0][:-1])
count_increase = 0
count_equal = 0
count_decrease = 0
for i in range(1, len(depths)):
    depth = int(depths[i][:-1])
    
    print(depth, end=": ")
    if depth > prev_depth:
        count_increase += 1
        print("increased")
    elif depth == prev_depth:
        count_equal += 1
        print("Same depth")
    else:
        count_decrease += 1
        print("decreased")

    prev_depth = depth

print(count_increase)
