"""
input has 3 values:
Card index | winning numbers | scratchcard numbers
if 0 winning numbers in the card, card score is 0
if 1, card score is 0
if above, (1st card) * 2^(n-1)

answer is the sum of all the card scores
"""

from typing import Set, Tuple

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

def parse_line(line: str):
    winning_numbers, card_numbers = line.strip().split(": ")[1].split(" | ")
    return set(map(int, winning_numbers.split())), set(map(int, card_numbers.split()))

def calc_card_score(numbers: Tuple[Set[int], Set[int]]):
    winning_numbers, card_numbers = numbers
    intersect = card_numbers.intersection(winning_numbers)
    return (len(intersect) > 0) * 2**(len(intersect) - 1)

parsed_lines = map(parse_line, lines)
print(sum(map(calc_card_score, parsed_lines)))
