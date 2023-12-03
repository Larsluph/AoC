# 10x10 grid
# end = 100 steps
# after each step:
#   cell += 1
#   if cell > 9:
#       flash() (increase every adjacent by 1)
#       cell = cell % 10

def next_step(oceanmap):
    for j in range(10):
        for x in range(10):
            oceanmap[j][i] += 1

with open("day11\\input.txt", 'r') as f:
    data = f.read().strip().split("\n")
    data = list(map(lambda x: list(map(int, x)), data))
    print(data)
