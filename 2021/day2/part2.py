with open("day2\\input.txt", 'r') as f:
    data = f.readlines()

x = 0
depth = 0
aim = 0

for instruct in data:
    ins, val = instruct.split(" ")
    val = int(val)
    
    if ins == "forward":
        x += val
        depth += (aim * val)

    elif ins == "up":
        aim -= val

    elif ins == "down":
        aim += val

    else:
        print("error")
        exit(0)

print(x*depth)
