word = input()
so = [chr(int(x)+97) for x in range(26)]
count=0

for s in so:
    for w in list(word):
        if s == w:
            count += 1
    print(count, end = ' ')
    count=0