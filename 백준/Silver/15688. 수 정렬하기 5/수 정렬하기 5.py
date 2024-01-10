import sys

n = input()
arr = list(map(int, sys.stdin.read().split()))

arr.sort()

for num in arr:
    print(num)