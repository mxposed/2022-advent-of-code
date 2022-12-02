
max_cal = 0
max_cal_elf = None
this_elf_cal = 0
elf_num = 1

for l in open("input", "r"):
    l = l.strip()
    if l:
        this_elf_cal += int(l)
    else:
        if this_elf_cal > max_cal:
            max_cal = this_elf_cal
            max_cal_elf = elf_num
        this_elf_cal = 0
        elf_num += 1

if this_elf_cal > max_cal:
    max_cal = this_elf_cal
    max_cal_elf = elf_num

print(f"Elf #{elf_num} carriest most calories: {max_cal}")

