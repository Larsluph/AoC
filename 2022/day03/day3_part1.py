total = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        data = line.strip()
        first = data[:len(data)//2]
        second = data[len(data)//2:]
        assert len(first) == len(second)

        intersect = set(first).intersection(set(second)).pop()
        assert isinstance(intersect, str) and len(intersect) == 1

        if intersect.islower():
            # 1-26
            total += ord(intersect) - ord('a') + 1
        elif intersect.isupper():
            # 27-52
            total += ord(intersect) - ord('A') + 27

print(total)
