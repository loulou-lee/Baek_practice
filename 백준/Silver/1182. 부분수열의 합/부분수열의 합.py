n, s = map(int, input().split())
inputarr = list(map(int, input().split()))

def func(x, current_sum):
    global result
    
    if x == n: 
        if current_sum == s:
            result += 1
        return

    func(x + 1, current_sum)  # x번째 원소를 포함하지 않는 경우
    func(x + 1, current_sum + inputarr[x])  # x번째 원소를 포함하는 경우

result = 0
func(0, 0)
if s ==0: result -= 1 # 공집합인 경우 제외
print(result)
