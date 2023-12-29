n = int(input())

stack = []

for _ in range(n):
    inp = int(input())
    if inp == 0: stack.pop()
    else: stack.append(inp)
        
d = len(stack)
sum = 0
for i in range(d):
    sum  += stack[i]
    
print(sum)