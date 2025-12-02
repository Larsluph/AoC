from collections import namedtuple
from pprint import pprint

ProductRange = namedtuple("ProductRange", "start,end")

with open('input.txt', encoding='ascii') as f:
    data = f.read().strip()

product_ranges = list(map(lambda x: ProductRange(*map(int, x.split('-'))), data.split(",")))

invalid = []
for product_range in product_ranges:
    for num in range(product_range.start, product_range.end+1):
        num_str = str(num)
        max_sample_size = len(num_str) // 2
        for chunk_size in range(1, max_sample_size+1):
            # extract all parts
            num_chunks = [num_str[i:i + chunk_size] for i in range(0, len(num_str), chunk_size)]
            checks = list(map(lambda chunk: num_chunks[0] == chunk, num_chunks))
            if all(checks):
                # print(num_str, num_str[:sample_size] == num_str[sample_size:])
                invalid.append(num)
                break

pprint(invalid)
print(sum(invalid))
