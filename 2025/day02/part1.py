from collections import namedtuple

ProductRange = namedtuple("ProductRange", "start,end")

with open('input.txt', encoding='ascii') as f:
    data = f.read().strip()

product_ranges = list(map(lambda x: ProductRange(*map(int, x.split('-'))), data.split(",")))

invalid = []
for product_range in product_ranges:
    for num in range(product_range.start, product_range.end+1):
        num_str = str(num)
        if len(num_str) % 2 == 1:
            continue
        sample_size = len(num_str) // 2
        if num_str[:sample_size] == num_str[sample_size:]:
            # print(num_str, num_str[:sample_size] == num_str[sample_size:])
            invalid.append(num)

print(sum(invalid))
