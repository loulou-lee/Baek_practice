num = int(input())

stack = []
result = []
count = 0

for x in range(num):
    
    n = int(input())
    
    while count < n:
        result.append('+')
        count += 1
        stack.append(count)
    
    if stack[-1] == n:
        stack.pop()
        result.append('-')

if len(stack) == 0:            
    for a in result: print(a)
else: print('NO')