# 계단 +1 or +2
# 1,2,3 연속으로 세개의 계단 못 밞음

n = int(input()) # 계단의 개수

step = [0]*n # 계단의 값 넣을 배열

for i in range(n): # 계단의 값 입력
    step[i] = int(input())
# 테이블 정의 
gum = [0]*(n+1) # 계단 갯수에 따른 최댓값 넣을 배열, gum[0]은 비워둠
# 점화식 만들기
# 초기 값을 채워넣기 
gum[1] = step[0] # 1
if n>=2: gum[2] = max(step[1], step[0]+step[1]) # 2
if n>=3: gum[3] = max(step[0]+step[2],step[1]+step[2]) # 2
# 반복문을 돌면서 배열을 채우기
if n>=3:
    for i in range(4,n+1):
        gum[i] = max(gum[i-2]+step[i-1], gum[i-3]+step[i-2]+step[i-1])
    
print(gum[n])