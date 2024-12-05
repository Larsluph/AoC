from collections import defaultdict

before_map = defaultdict(list)
after_map = defaultdict(list)
pages = []

step = 0
with open('input.txt', encoding='ascii') as f:
    for line in f.readlines():
        if not line.strip():
            step += 1
            continue

        if step == 0:
            a, b = line.strip().split('|')
            after_map[a].append(b)
            before_map[b].append(a)
        elif step == 1:
            pages.append(line.strip().split(','))

total_count = 0
total = 0
for page in pages:
    iter_count = 0
    check = True
    loop = True
    while loop:
        loop = False
        for i, digit in enumerate(page):
            for before_digit in page[:i]:
                if digit in before_map[before_digit]:
                    loop = True
                    check = False
                    page[i], page[i-1] = page[i-1], page[i]
                    break

            for after_digit in page[i+1:]:
                if digit in after_map[after_digit]:
                    loop = True
                    check = False
                    page[i], page[i+1] = page[i+1], page[i]
                    break

    if not check:
        total_count += 1
        total += int(page[len(page) // 2])
        print(int(page[len(page) // 2]))

print(total_count)
print(total)
