
max_cal = [0, 0, 0]
this_elf_cal = 0

for l in open("input", "r"):
    l = l.strip()
    if l:
        this_elf_cal += int(l)
    else:
        if this_elf_cal > max_cal[0]:
            max_cal[0] = this_elf_cal
            max_cal = list(sorted(max_cal))

        this_elf_cal = 0


print(f"Most calories: {max_cal}, {sum(max_cal)}")

