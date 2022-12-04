

cnt = 0
for l in open("input"):
    l = l.strip()
    e1, e2 = l.split(",")
    e1s, e1e = e1.split("-")
    e2s, e2e = e2.split("-")
    e1s, e1e, e2s, e2e = int(e1s), int(e1e), int(e2s), int(e2e)
    if e1s <= e2s and e1e >= e2e:
        cnt += 1
    elif e2s <= e1s and e2e >= e1e:
        cnt += 1

print(f"Number of contained ranges {cnt}")

