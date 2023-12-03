count = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        range1, range2 = line.strip().split(',')
        
        min1, max1 = map(int, range1.split('-'))
        min2, max2 = map(int, range2.split('-'))
        
        set1 = set(range(min1, max1+1))
        set2 = set(range(min2, max2+1))

        # if 2 fully contains 1 or 1 fully contains 2
        if len(set1.intersection(set2)):
            count += 1

print(count)
