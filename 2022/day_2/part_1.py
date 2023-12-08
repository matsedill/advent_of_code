def read_input():
    with open("./input1", "r") as f:
        return f.read()


ROCK = "X"
PAPER = "Y"
SCISSOR = "Z"

O_ROCK = "A"
O_PAPER = "B"
O_SCISSOR = "C"

SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def you_win(opponent, you):

    if you == ROCK and opponent == O_SCISSOR:
        return True
    if you == SCISSOR and opponent == O_PAPER:
        return True
    if you == PAPER and opponent == O_ROCK:
        return True
    return False

def calculate_score(opponent, you):
    DRAW = 3
    WIN = 6
    score = SCORES[you]
    if opponent+you in [O_SCISSOR+SCISSOR, O_PAPER+PAPER, O_ROCK+ROCK]:
        return score + DRAW
    if you_win(opponent, you):
        return score + WIN
    return score

def main():
    input = read_input()
    scores = 0
    for line in input.splitlines():
        scores += calculate_score(*line.split(' '))
    print(scores)

if __name__ == "__main__":
    main()
