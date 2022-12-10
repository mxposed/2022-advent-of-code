
dir_info = {}

path = None

for l in open("input"):
    l = l.strip()
    if l.startswith("$"):
        cmd = l[2:]
        if cmd.startswith("cd "):
            cur_dir = cmd[3:]
            if cur_dir == "/":
                path = [""]
            elif cur_dir.startswith("/"):
                path = [cur_dir]
            elif cur_dir == "..":
                path = path[:-1]
            else:
                path.append(cur_dir)
            cur_dir = "/".join(path)
            if cur_dir not in dir_info:
                dir_info[cur_dir] = dict(size=0, children=[])
                print(f"Added {cur_dir}")
    else:
        i1, i2 = l.split(" ")
        if i1 == "dir":
            dir_info[cur_dir]["children"].append(cur_dir + "/" + i2)
        else:
            dir_info[cur_dir]["size"] += int(i1)

for d in sorted(dir_info.keys(), key=lambda x: len(x), reverse=True):
    for c_d in dir_info[d]["children"]:
        dir_info[d]["size"] += dir_info[c_d]["size"]


MAX_DIR_SIZE = 100_000

cnt = 0
for d in dir_info.keys():
    if dir_info[d]["size"] < MAX_DIR_SIZE:
        cnt += dir_info[d]["size"]

print(cnt)


