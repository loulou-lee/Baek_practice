import sys

input = sys.stdin.readline

arr = []

n = int(input())

for i in range(n):
    m, k = map(int, input().split())
    arr.append((m, k))

def setting(arr):
    return arr[0], arr[1]

arr = sorted(arr, key=setting)

for arr in arr:
    print(arr[0], arr[1])