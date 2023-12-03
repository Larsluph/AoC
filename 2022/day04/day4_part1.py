count = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        range1, range2 = line.strip().split(',')
        
        min1, max1 = map(int, range1.split('-'))
        min2, max2 = map(int, range2.split('-'))

        # if 2 fully contains 1 or 1 fully contains 2
        if min1 <= min2 and max1 >= max2 or min2 <= min1 and max2 >= max1:
            count += 1

print(count)
