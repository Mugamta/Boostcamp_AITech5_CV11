import sys
N = int(input()) #기둥의 개수 N
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N)) # L(기둥의 왼쪽 면의 위치), H(기둥의 높이)
arr.sort() #기둥들을 왼쪽 면의 위치 기준으로 오름차순 정렬

max = [0,0] # 가장 높은 기둥의 정보 저장
for i in range(N) :
    L, H = arr[i]
    if H > max[1] :  #max update
        max[1] = H
        max[0] = L
        max_idx = i
answer = max[1]
# print(f"max = [{max[0]},{max[1]}, answer={answer}]")
#left 
temp_max = 0
for i in range(max_idx) :
    
    L, H = arr[i]
    if H > temp_max :
        answer += (H - temp_max) * (max[0]-L)
        temp_max = H
    # print(f"i={i}, L={L},H={H}, answer ={answer}")
#right
temp_max = 0
for i in range(N-max_idx-1) : 
    ii = N - i - 1 
    L, H  = arr[ii]
    if H > temp_max :
        answer += (H - temp_max) * (L - max[0])
        temp_max = H
    # print(f"i={i}, L={L},H={H}, answer ={answer}")
    
    

print(answer)

