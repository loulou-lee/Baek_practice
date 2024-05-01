n = int(input())
d = [0]*12
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(n):
    result = int(input())
    if result == 1: print(d[1])
    elif result == 2: print(d[2])
    elif result == 3: print(d[3])
    else:
        for j in range(4,result+1):
            d[j] = d[j-1] + d[j-2] + d[j-3]
        print(d[result])
