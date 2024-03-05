import sys
from collections import deque

n, m = map(int, input().split())

g = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]

def move():
    
    queue = deque([(0,0)])
    
    while queue:
        
        v = queue.popleft()

        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        
        for i in range(4):
            
            nx = v[0]+dx[i]
            ny = v[1]+dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                
            if g[nx][ny] == 0: continue
                
            if g[nx][ny] == 1:

                g[nx][ny] = g[v[0]][v[1]] + 1

                queue.append((nx, ny))
    
    return g[n-1][m-1]
                    
print(move())