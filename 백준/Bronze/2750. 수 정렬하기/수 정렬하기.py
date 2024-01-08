import sys

n=int(input())
arr = []

for i in range(n):
    inpu = sys.stdin.readline()
    arr.append(int(inpu))

arr.sort()

for number in arr:
    print(number)