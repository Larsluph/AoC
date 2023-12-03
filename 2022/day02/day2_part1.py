with open("input.txt", 'r') as f:
    lines = list(map(lambda x: x.strip().split(" "), f.readlines()))

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6


def parse_a(x: str) -> int:
    return "ABC".index(x) + 1


def parse_b(x: str) -> int:
    return "XYZ".index(x) + 1


def check_win(a: int, b: int) -> int:
    return a == ROCK and b == PAPER or a == PAPER and b == SCISSORS or a == SCISSORS and b == ROCK


def check_draw(a: int, b: int) -> int:
    return a == b


def get_score(a: str, b: str) -> int:
    data = parse_a(a), parse_b(b)

    if check_win(*data):
        return WIN
    elif check_draw(*data):
        return DRAW
    else:
        return LOSS


if __name__ == '__main__':
    score = 0
    for a, b in lines:
        score += parse_b(b) + get_score(a, b)
    print(score)
