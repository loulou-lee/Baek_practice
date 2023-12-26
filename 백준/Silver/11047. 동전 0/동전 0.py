n, hap = map(int, input().split())

coin=[]
count=0

for i in range(n):
    coin.append(input())
    
coin.reverse()
    
for co in coin:
    count += hap // int(co)
    hap %= int(co)
    
print(count)