import sys

n, m = map(int, input().split()) # 수의 개수 n, 합을 구해야 하는 횟수 m

ar = list(map(int, input().split()))

for i in range(1,n): # i번째까지 더한 값을 ar에 할당
    ar[i] = ar[i] + ar[i-1]
    
for i in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1: print(ar[j-1])
    else: print(ar[j-1] - ar[i-2])