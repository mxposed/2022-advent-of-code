

buf = open("input").read().strip()

i = 0
while True:
    sub = buf[i:i+4]
    if len(set(sub)) == 4:
        print(i + 4)
        break
    i += 1

