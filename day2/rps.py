

PICK_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

GAME_SCORE = {
    "lost": 0,
    "draw": 3,
    "win": 6
}


def game_outcome(p1, p2):
    if p1 == "A":
        if p2 == "X":
            return "draw"
        if p2 == "Y":
            return "win"
        return "lost"
    if p1 == "B":
        if p2 == "X":
            return "lost"
        if p2 == "Y":
            return "draw"
        return "win"
    if p2 == "X":
        return "win"
    if p2 == "Y":
        return "lost"
    return "draw"


total_score = 0
for l in open("input"):
    l = l.strip()
    if not l:
        continue
    p1, p2 = l.split()
    total_score += PICK_SCORE[p2] + GAME_SCORE[game_outcome(p1, p2)]

print(f"Your total score is {total_score}")


