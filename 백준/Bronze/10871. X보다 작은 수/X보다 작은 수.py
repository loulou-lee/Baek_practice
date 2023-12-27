n, x = map(int, input().split())
li = list(map(int, input().split()))

for l in li:
	if l < x:
		print(l, end=' ')