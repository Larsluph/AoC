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


def parse_requirement(x: str) -> int:
    return "XYZ".index(x) * 3


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


def predict_b(a: int, score: int) -> int:
    if score == WIN:
        b = a % 3
    elif score == DRAW:
        b = a - 1
    else:
        b = (a - 2) % 3

    return "XYZ"[b]


if __name__ == '__main__':
    score = 0
    with open("input.txt", 'r') as f:
        lines = list(map(lambda x: x.strip().split(" "), f.readlines()))

    for opponent, requirement in lines:
        a = parse_a(opponent)
        x = parse_requirement(requirement)
        player = predict_b(a, x)
        b = parse_b(player)
        score += b + get_score(opponent, player)
    print(score)
