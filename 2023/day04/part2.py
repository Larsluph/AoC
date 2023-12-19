"""
input has 3 values:
Card index | winning numbers | scratchcard numbers
you win a copy of the n following cards

the answer should be the number of total cards you gathered
"""

from collections import defaultdict
from typing import Set, Tuple

with open('input.txt', encoding='ascii') as f:
    lines = f.readlines()

def parse_line(line: str):
    winning_numbers, card_numbers = line.strip().split(": ")[1].split(" | ")
    return set(map(int, winning_numbers.split())), set(map(int, card_numbers.split()))

def calc_card_score(numbers: Tuple[Set[int], Set[int]]):
    winning_numbers, card_numbers = numbers
    return len(card_numbers.intersection(winning_numbers))

parsed_lines = map(parse_line, lines)

card_counts = defaultdict(lambda: 1)
for i, score in enumerate(map(calc_card_score, parsed_lines), start=1):
    for j in range(i, i+score):
        card_counts[j+1] += card_counts[i]
print(sum(card_counts.values() + 1))
