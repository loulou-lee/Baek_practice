import sys

input = sys.stdin.readline
n = int(input())

data = dict()

for i in range(n):
    m, k = input().split()
    if k == 'enter':
        data[m] = 1
    else:
        data[m] = 0

arr = []

for key, value in data.items():
    if 1 == value:
        arr.append(key)
        
arr.sort()
arr.reverse()

for data in arr:
    print(data)