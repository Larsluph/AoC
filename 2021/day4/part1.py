import re

pattern = re.compile(r"\d+")

def sum_board(grid, check):
    sum = 0
    for y in range(5):
        for x in range(5):
            if not check[y][x]:
                sum += grid[y][x]
    return sum

with open("day4\\input.txt", 'r') as f:
    picks = list(map(int, f.readline().split(",")))

    # map grids
    grids = list()
    checks = list()

    # get bingo roll
    while len(grids) < 100:
        f.readline()

        grid = list()
        check = list()

        for i in range(5):
            line = f.readline().strip()
            match = list(map(int, pattern.findall(line)))
            grid.append(match)
            check.append([0]*5)

        grids.append(grid)
        checks.append(check)

winners = list()
for pick in picks:
    for i, (grid, check) in enumerate(zip(grids, checks)):
        for y in range(5):
            for x in range(5):
                # check for match
                if grid[y][x] == pick:
                    check[y][x] = True

        # check for vertical match
        for y in range(5):
            if all(check[y]):
                if i not in winners:
                    winners.append(i)
        for x in range(5):
            temp = list()
            for y in range(5):
                temp.append(check[y][x])
            if all(temp):
                if i not in winners:
                    winners.append(i)
                    board_sum = sum_board(grid, check)
                    print(pick, "*", board_sum, "=", pick*board_sum)

print(f"winners: {winners}")

print(f"first winner: {winners[0]}")
print(f"last winner: {winners[-1]}")
