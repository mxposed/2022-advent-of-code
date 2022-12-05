


stacks = []


for l in open("input"):
    l = l.strip()
    if l.startswith("["):
        i = 0
        crate_n = 0
        while i < len(l):
            if len(stacks) <= crate_n:
                stacks.append([])
            if l[i] == "[":
                crate = l[i + 1]
                stacks[crate_n] = [crate] + stacks[crate_n]
            crate_n += 1
            i += 4
    if l.startswith("move"):
        data = l.split(" ")
        how_many = int(data[1])
        from_i = int(data[3]) - 1
        to_i = int(data[5]) - 1
        move_part = stacks[from_i][-how_many:]
        stacks[from_i] = stacks[from_i][:-how_many]
        stacks[to_i] = stacks[to_i] + move_part

print(repr(stacks))
print("".join([x[-1] for x in stacks]))

