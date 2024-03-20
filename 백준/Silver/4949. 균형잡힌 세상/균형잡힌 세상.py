import sys

while True:
    #input = sys.stdin.readline
    a=input().rstrip()
    if a == '.':
        break
    a = list(a)

    stack = []
    isValid = True

    for i in a:
        if i == '(':
            stack.append('(')

        if i == ')':
            if len(stack)==0 or stack[len(stack)-1] != '(':
                isValid = False
                continue

            stack.pop() 

        if i == '[':
            stack.append('[')

        if i == ']':
            if len(stack)==0 or stack[len(stack)-1] != '[':
                isValid = False
                continue

            stack.pop() 

        if i == '.':
            if len(stack) != 0: isValid = False

            if isValid: print('yes')
            else: print('no')