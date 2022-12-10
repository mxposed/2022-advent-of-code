

status = {}

knots = [(0, 0)] * 10

status[knots[-1]] = True

def move_tail(h, t):
    # vertical movement
    if t[0] == h[0] and (t[1] - h[1]) in [-2, 2]:
        return (t[0], t[1] - (t[1] - h[1]) // 2)
    # horizontal movement
    if t[1] == h[1] and (t[0] - h[0]) in [-2, 2]:
        return (t[0] - (t[0] - h[0]) // 2, t[1])
    # diagonal vertical
    if (t[0] - h[0]) in [-1, 1] and (t[1] - h[1]) in [-2, 2]:
        return (h[0], (t[1] + h[1]) // 2)
    # diagonal horizontal
    if (t[1] - h[1]) in [-1, 1] and (t[0] - h[0]) in [-2, 2]:
        return ((t[0] + h[0]) // 2, h[1])
    # diagonal diagonal
    if (t[0] - h[0]) in [-2, 2] and (t[1] - h[1]) in [-2, 2]:
        return ((t[0] + h[0]) // 2, (t[1] + h[1]) // 2)
    return t

for l in open("input"):
    cmd, d = l.strip().split()
    for i in range(int(d)):
        if cmd == "U":
            knots[0] = (knots[0][0] - 1, knots[0][1])
        if cmd == "D":
            knots[0] = (knots[0][0] + 1, knots[0][1])
        if cmd == "R":
            knots[0] = (knots[0][0], knots[0][1] + 1)
        if cmd == "L":
            knots[0] = (knots[0][0], knots[0][1] - 1)
        for i in range(1, len(knots)):
            prev_knot = knots[i - 1]
            knot = knots[i]
            knots[i] = move_tail(prev_knot, knot)
        status[knots[-1]] = True
        print(knots)



print(len(status))
