import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

arr = [[] for _ in range(m)]

for i in range(n):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
  
count = 0
visited = [False] * m
for i in range(m):
    if not visited[i]:
        bfs(arr, i, visited)
        count += 1
        
print(count)