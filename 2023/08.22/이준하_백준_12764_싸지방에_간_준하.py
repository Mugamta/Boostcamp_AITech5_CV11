import sys 
import heapq

input = sys.stdin.readline

n = int(input())

heap = []
com = [0 for _ in range(n)] # 총 컴퓨터
user_num = [0 for _ in range(n)] # 좌석별 사용한 사람 수
min_com = 0 # 사용한 컴퓨터 수

for _ in range(n):
    p,q = map(int, input().split())
    heapq.heappush(heap,[p,q])
    
while heap:
    temp = heapq.heappop(heap) #가장 번호가 작은 자리부터 순서대로
    for i in range(len(com)):
        if com[i] <= temp[0]: # 시작시각에 컴이 비어있으면,
            if com[i] == 0: # 컴을 처음 쓰면
                min_com += 1 # com 사용 수 증가
            com[i] = temp[1] # com 작은 것 부터
            user_num[i] += 1
            break
print(min_com)

for i in user_num:
    if i != 0:
        print(i, end = ' ')