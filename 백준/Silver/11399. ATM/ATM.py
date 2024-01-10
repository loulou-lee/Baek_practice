import sys

#각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분
n = int(input())
arr = list(map(int, sys.stdin.readline().split())) #list(map(int, input().split()))

arr.sort()

sum=0

for i in range(n):
    sum+=arr[i]*(n-i)
    
print(sum)