# 11시 15분 시작
# 11시 20분 문제 이해
# 11시 49분 한칸 탐색 구현
# 1시 19분 첫번쨰 제출 -> 78%에서 시간 초과
# 어떻게 해결해야할까요?



import sys

N, L, R = map(int, sys.stdin.readline().split())

array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def find(result):
    for x,y in result:
        center = array[x][y]
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            x_i = x+dx[i]
            y_i = y+dy[i]
            if [x_i,y_i] in result:
                continue
            if x_i <= -1 or y_i <= -1 or x_i >= N or y_i >= N:
                continue
            else:
                side = array[x_i][y_i]
            dev = abs(center-side)
            if dev >= L and dev <= R :
                result.append([x_i,y_i])
    return result

def once():
    temp = []
    result = []
    for i in range(N):
        for j in range(N):
            if [i,j] not in temp:
                ally = find([[i,j]])
                temp.extend(ally)
                if len(ally) != 1:
                    result.append(ally)
    return result

cnt = 0
while True:
    one = once()

    if not one:
        print(cnt)
        break

    for j in one:
        len_i = len(j)
        ally_t = 0
        for k in j:
            ally_t += array[k[0]][k[1]]
        aver = ally_t/len_i
        for x,y in j:
            array[x][y] = int(aver)
    cnt += 1


