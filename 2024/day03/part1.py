import re

with open('input.txt', encoding='ascii') as f:
    memory = f.read()

mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

matches = mul_pattern.findall(memory)
total = sum((int(a)*int(b) for a,b in matches))
print(total)
