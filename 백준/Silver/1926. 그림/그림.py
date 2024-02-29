import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
def dfs(x,y):
    global vol
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        vol += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result=0
vol=0
v=[]
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            v.append(vol)
            vol=0
            
print(result)
if result == 0:
    print(0)
else:
    print(max(v))