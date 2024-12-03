import re

with open('input.txt', encoding='ascii') as f:
    memory = f.read()

MAX_VALUE = len(memory)+1

mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
mul_matches = mul_pattern.finditer(memory)
next_mul = next(mul_matches)

enable_pattern = re.compile(r"do\(\)")
enable_matches = enable_pattern.finditer(memory)
enable_consumed: bool = False
next_enable: int = -1
next_enable = next(enable_matches)

disable_pattern = re.compile(r"don\'t\(\)")
disable_matches = disable_pattern.finditer(memory)
disable_consumed: bool = False
next_disable: int = -1
next_disable = next(disable_matches)

enable_flag = True
total = 0

while True:
    next_values = [
        ("mul", next_mul.start()),
        ("enable", MAX_VALUE if enable_consumed else next_enable.start()),
        ("disable", MAX_VALUE if disable_consumed else next_disable.start())
    ]

    lower_value = max(next_values, key=lambda x: x[1])

    match lower_value[0]:
        case "mul":
            if enable_flag:
                a, b = next_mul.groups()
                total += int(a) * int(b)

            try:
                next_mul = next(mul_matches)
            except StopIteration:
                break
        case "enable":
            enable_flag = True
            if not enable_consumed:
                try:
                    next_enable = next(enable_matches)
                except StopIteration:
                    enable_consumed = True
        case "disable":
            enable_flag = False
            if not disable_consumed:
                try:
                    next_disable = next(disable_matches)
                except StopIteration:
                    disable_consumed = True

print(total)
