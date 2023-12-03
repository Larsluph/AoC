with open("day2\\input.txt", 'r') as f:
    data = f.readlines()

x = 0
depth = 0

for instruct in data:
    ins, val = instruct.split(" ")
    val = int(val)
    
    if ins == "forward":
        x += val
        
    elif ins == "up":
        depth -= val
        
    elif ins == "down":
        depth += val

    else:
        print("error")
        exit(0)

print(x*depth)
