import sys

a, b, c = map(int, sys.stdin.read().split())

checks = list(str(a*b*c))

num = [str(i) for i in range(0,10)]

for i in num:
    count = 0
    for check in checks:
        if i == check:
            count += 1 
    print(count)