

trees = open("input").read().strip().split("\n")

trees = [list(map(int, x)) for x in trees]

status = {}

H = len(trees)
W = len(trees[0])

# from top
for i in range(H):
    for j in range(W):
        tree = trees[i][j]
        # go top
        top_score = 0
        for i2 in range(i - 1, -1, -1):
            next_tree = trees[i2][j]
            top_score += 1
            if next_tree >= tree:
                break

        bottom_score = 0
        for i2 in range(i + 1, H):
            next_tree = trees[i2][j]
            bottom_score += 1
            if next_tree >= tree:
                break

        left_score = 0
        for j2 in range(j - 1, -1, -1):
            next_tree = trees[i][j2]
            left_score += 1
            if next_tree >= tree:
                break

        right_score = 0
        for j2 in range(j + 1, W):
            next_tree = trees[i][j2]
            right_score += 1
            if next_tree >= tree:
                break
        
        status[(i, j)] = top_score * bottom_score * left_score * right_score


print(max(status.values()))

