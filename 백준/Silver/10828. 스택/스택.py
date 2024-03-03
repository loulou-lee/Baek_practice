'''
스택에서는 제일 상단이 아닌 나머지 원소들의 확인/변경 기능이 제공되지 않음
그리고 스택을 활용하는 예시들을 보면 애초에 제일 상단이 아닌 나머지 원소들의 확인/변경이 필요하지 않음
하지만 배열을 이용해 스택을 구현하면 기본적인 스택의 기능 이외에도 제일 상단이 아닌 나머지 원소들의 확인/변경을 가능
'''

import sys

n = int(input()) # 첫째 줄에 주어지는 명령의 수 n (1 ≤ n ≤ 10,000)

stack = [0]*10005
top = 0 # top 위치, 다음에 원소가 추가될 때 삽입해야하는 곳

for _ in range(n):
    
    inp = sys.stdin.readline().rstrip()
    if len(inp)>5: m, x = inp.split()
    else: m = inp
    
    if m=='push': # push X: 정수 X를 스택에 넣는 연산이다.
        stack[top] = int(x) # 정수형으로
        top += 1
        
    elif m=='pop':
        if top > 0:
            top -= 1
            p = stack[top]
            print(p)
        else: print(-1)
        
    elif m=='size': print(top)
        
    elif m=='empty':
        if top == 0: print(1)
        else: print(0)
        
    elif m=='top':
        if top == 0: print(-1)
        else: print(stack[top-1])