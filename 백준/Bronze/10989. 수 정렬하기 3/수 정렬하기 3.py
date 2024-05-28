# 계수정렬
## 메모리 초과
import sys
input = sys.stdin.readline

n = int(input())

check = [0]*(10000)

for _ in range(n):
    x = int(input()) - 1
    check[x] = check[x]+1
    
for i in range(1,10000+1):
    for _ in range(check[i-1]):
        print(i)