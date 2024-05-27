import sys

n = int(input()) # 첫째 줄에 주어지는 명령의 수 n (1 ≤ n ≤ 2,000,000)

q = [0]*2000005
front = 0 # front 위치, 
back = 0 # back 다음에 원소가 추가될 때 삽입해야하는 곳, rear

for _ in range(n):
    
    inp = sys.stdin.readline().rstrip()
    if len(inp)>5: m, x = inp.split()
    else: m = inp
    
    if m=='push': # push X: 정수 X를 큐에 넣는 연산이다
        q[back] = int(x) # 정수형으로
        back += 1
        
    elif m=='pop': # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if front == back:
            print(-1)
        else: 
            p = q[front]
            front += 1
            print(p)
        
    elif m=='size': print(back-front) # size: 큐에 들어있는 정수의 개수를 출력한다.
        
    elif m=='empty': # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if front == back: print(1)
        else: print(0)
        
    elif m=='front': # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if front == back: print(-1)
        else: print(q[front])
            
    elif m=='back': # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if front == back: print(-1)
        else: print(q[back-1])