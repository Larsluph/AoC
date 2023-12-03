total = 0

with open('input.txt', 'r') as f:
    while elf1 := f.readline().strip():
        elf2 = f.readline().strip()
        elf3 = f.readline().strip()

        intersect = set(elf1).intersection(set(elf2), set(elf3)).pop()
        assert isinstance(intersect, str) and len(intersect) == 1

        if intersect.islower():
            # 1-26
            total += ord(intersect) - ord('a') + 1
        elif intersect.isupper():
            # 27-52
            total += ord(intersect) - ord('A') + 27

print(total)
