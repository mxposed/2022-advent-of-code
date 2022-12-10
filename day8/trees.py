

trees = open("input").read().strip().split("\n")

trees = [list(map(int, x)) for x in trees]

status = {}

H = len(trees)
W = len(trees[0])

# from top
prev_max = [-1] * W
for i in range(H):
    for j in range(W):
        tree = trees[i][j]
        if tree > prev_max[j]:
            status[(i, j)] = True
            prev_max[j] = tree

# from bottom
prev_max = [-1] * W
for i in range(H - 1, -1, -1):
    for j in range(W):
        tree = trees[i][j]
        if tree > prev_max[j]:
            status[(i, j)] = True
            prev_max[j] = tree

# from left
prev_max = [-1] * H
for j in range(W):
    for i in range(H):
        tree = trees[i][j]
        if tree > prev_max[i]:
            status[(i, j)] = True
            prev_max[i] = tree

# from right
prev_max = [-1] * H
for j in range(W - 1, -1, -1):
    for i in range(H):
        tree = trees[i][j]
        if tree > prev_max[i]:
            status[(i, j)] = True
            prev_max[i] = tree

print(len(status))


