

PRIORITIES = {}
i = ord("a")
z = ord("z")
s = 1

while True:
    PRIORITIES[chr(i)] = s
    s += 1
    if i == z:
        break
    i += 1

i = ord("A")
z = ord("Z")

while True:
    PRIORITIES[chr(i)] = s
    if i == z:
        break
    i += 1
    s += 1


cnt = 0
lines = open("input").readlines()
i = 0
while i < len(lines):
    p1 = lines[i].strip()
    p2 = lines[i + 1].strip()
    p3 = lines[i + 2].strip()
    item = list(set(p1) & set(p2) & set(p3))
    assert len(item) == 1
    item = item[0]
    cnt += PRIORITIES[item]
    i += 3

print(f"Total priorities of badges: {cnt}")

