import sys

N, X = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


answer = sum(arr[:X])
temp = answer
num = 1


for n in range(N-X) :
    temp = temp -arr[n] + arr[n+X]
    if temp > answer :
        answer = temp 
        num = 1
    elif temp == answer :
        num += 1
    
if answer :  # 방문자 수가 0이 아니면
    print(answer) # 최대 방문자 수 출력
    print(num) #기간 개수 출력
else : # 방문자 수가 0 이면
    print('SAD') # SAD 출력
