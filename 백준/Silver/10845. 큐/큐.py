import sys

def push(tail, x): #정수 X를 큐에 넣는 연산이다.
    queue[tail] = x
    tail += 1
    return tail
    
def pop(head): #큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if head == tail: print(-1)
    else: 
        print(queue[head])
        head += 1
    return head
    
def front(): #큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if head == tail: print(-1)
    else: print(queue[head])
    
def back(): #큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if head == tail: print(-1)
    else: print(queue[tail-1])

n = int(input()) # 첫째 줄에 주어지는 명령의 수 n (1 ≤ n ≤ 10,000)

queue = [0]*10005
head = 0
tail = 0

for _ in range(n):
    
    input = sys.stdin.readline
    m = input().split()
    
    if m[0]=='push': # push X: 정수 X를 스택에 넣는 연산이다.
        tail = push(tail, m[1])
        
    elif m[0]=='pop':
        head = pop(head)
        
    elif m[0]=='size': 
        print(tail-head)
        
    elif m[0]=='empty':
        if head == tail: print(1)
        else: print(0)
        
    elif m[0]=='front':
        front()
            
    elif m[0]=='back':
        back()