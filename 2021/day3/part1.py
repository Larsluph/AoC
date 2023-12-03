with open("day3\\input.txt", 'r') as f:
    lines = f.readlines()

gamma_rate = ""
epsilon_rate = 0

for i in range(len(lines[0])-1):
    count_0 = 0
    count_1 = 0

    for line in lines:
        if line[i] == "0":
            count_0 += 1
        elif line[i] == "1":
            count_1 += 1

    if count_0 > count_1:
        print("higher rate: 0")
        gamma_rate += "0"
    else:
        print("higher rate: 1")
        gamma_rate += "1"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = gamma_rate ^ (2**(len(lines[0])-1) - 1)

print(gamma_rate, epsilon_rate)
print(gamma_rate * epsilon_rate)
