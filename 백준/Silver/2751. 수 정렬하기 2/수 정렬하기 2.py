import sys
n = input()
arr = list(map(int, sys.stdin.read().split()))

arr.sort()

for number in arr:
    print(number)