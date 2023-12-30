from collections import deque # queue 라이브러리를 이용하는 것보다 간단하다.

n = int(input())

queue = deque()

for i in range(n):
    queue.append(i+1)

if n > 2:
    for _ in range(n-2):
        queue.popleft()
        a=queue.popleft()
        queue.append(a)


if n%2==0:
    queue.popleft()
    a=queue.popleft()
    queue.append(a)
    print(queue.popleft())
elif n==1: print(queue.popleft())
else:
    queue.popleft()
    print(queue.popleft())