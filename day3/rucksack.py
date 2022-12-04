

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
for l in open("input"):
    l = l.strip()
    p1, p2 = l[:len(l) // 2], l[len(l) // 2:]
    item = list(set(p1) & set(p2))
    assert len(item) == 1
    item = item[0]
    cnt += PRIORITIES[item]
    
print(f"Total priorities: {cnt}")

