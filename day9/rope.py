

status = {}

head = [0, 0]
tail = (0, 0)

status[tail] = True

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
    if (t[1] - h[1]) in [-1, 1] and (t[0] - h[0]) in [-2, 2]:
        return ((t[0] + h[0]) // 2, h[1])
    return t

for l in open("input"):
    cmd, d = l.strip().split()
    for i in range(int(d)):
        if cmd == "U":
            head[0] -= 1
        if cmd == "D":
            head[0] += 1
        if cmd == "R":
            head[1] += 1
        if cmd == "L":
            head[1] -= 1
        tail = move_tail(head, tail)
        status[tail] = True

print(len(status))
