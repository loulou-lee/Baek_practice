import sys
import re

input = sys.stdin.readline
n = int(input())
arr = sys.stdin.read().split()

for i in range(n):
    for j in range(i+1,n):
        if len(arr[i]) > len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
        elif len(arr[i]) == len(arr[j]):
            numberi = re.sub(r'[^0-9]', '', arr[i])
            numberj = re.sub(r'[^0-9]', '', arr[j])
            numberi = sum(map(int, numberi))
            numberj = sum(map(int, numberj))
            if numberi > numberj:
                arr[i], arr[j] = arr[j], arr[i]
            elif numberi == numberj: # 길이가 같고 합도 같으면
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

for x in arr:                    
    print(x)