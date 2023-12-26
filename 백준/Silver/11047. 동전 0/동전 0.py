n, N = map(int, input().split())

count=0

coin = [int(input()) for _ in range(n)]

coin.reverse()

for coin in coin:
    if N//coin > 0:
        count += N//coin
        N %= coin

print(count)