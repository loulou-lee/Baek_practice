import sys
input = sys.stdin.readline

n = int(input())

data = []

for i in range(n):
    m, k = input().split()
    data.append((int(m), k))

def setting(data):
    return data[0]
    
result = sorted(data, key=setting)
for result in result:
    print(result[0], result[1])