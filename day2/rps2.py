

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


def pick_for_outcome(p1, outcome):
    p2 = outcome
    if p1 == "A": # rock
        if p2 == "X":
            return "Z"
        if p2 == "Y":
            return "X"
        return "Y"
    if p1 == "B": # paper
        if p2 == "X":
            return "X"
        if p2 == "Y":
            return "Y"
        return "Z"
    if p2 == "X":
        return "Y"
    if p2 == "Y":
        return "Z"
    return "X"



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
    p1, o = l.split()
    p2 = pick_for_outcome(p1, o)
    total_score += PICK_SCORE[p2] + GAME_SCORE[game_outcome(p1, p2)]

print(f"Your total score is {total_score}")


