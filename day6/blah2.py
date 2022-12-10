

buf = open("input").read().strip()

i = 0
while True:
    sub = buf[i:i+14]
    if len(set(sub)) == 14:
        print(i + 14)
        break
    i += 1

