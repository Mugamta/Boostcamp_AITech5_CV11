# 1:00 시작
# 1:15 문제 이해

# 1.입력 이해
    # 1. 격자크기, 파이어볼 정보 수, 이동 수
    # 2. 파이어볼 정보 = y좌표, x좌표, 질량, 방향, 속력
# 2. 구현 해야할 것
    # 1. 이동
    # 2. 이동 결과, 파이어볼이 같은 좌표에 있는 경우
        # 1. 파이어볼 수, 파이어볼의 질량 합, 속력 합 구하기
        # 2. 질량, 속력 계산
        # 3. 이전 파이어볼의 방향 통일 여부 확인하여, 이후 파이어볼의 방향 설정
        # 4. 이동 수 만큼 반복하며 확인 할 것
            # 1. 질량이 0인 경우 소멸
            # 2. 반복이 끝나면, 남은 파이어볼 질량의 합 출력

# 1:20 입력 정의
# 1:36 이동 구현
# 1:48 만나는 경우 구현
# 2:10 안만나는 경우 및 질량 합 출력 구현
# 2:12 테스트케이스 8, 16, 16, 30 디버깅 필요
# 2:36 기존 for m,s,d in world: 를 world.pop()으로 변경하여 디버깅 성공


import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
world = [[[] for _ in range(N)] for _ in range(N)]
directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
fireballs = [list(map(int,input().split())) for _ in range(M)]

for _ in range(K):
    # fireball 이동
    while fireballs:
        y,x,m,s,d = fireballs.pop()
        x_ = (x + s*directions[d][0]) % N
        y_ = (y + s*directions[d][1]) % N
        world[y_][x_].append([m,s,d])
    
    # 만났는지 체크
    for x in range(N):
        for y in range(N):
            cnt = len(world[y][x])
            # 만났으면, 4개로 쪼개고, 정보 등록
            if cnt > 1 :
                sum_m = 0
                sum_s = 0
                odd = 0
                while world[y][x]:
                    m,s,d = world[y][x].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2:
                        odd +=1
                # 모두 같은 홀수 또는 짝수인지 비교하여 방향 설정
                if cnt==odd or odd == 0:
                    d = [0,2,4,6]
                else:
                    d = [1,3,5,7]
                # 질량 및 속도 설정
                m = sum_m//5
                s = sum_s//cnt
                # 질량이 남아있으면, 생성된 fireball 등록, 없으면 소멸
                if m:
                    fireballs.extend([[y,x,m,s,i] for i in d])

            # 안만나면, 현재 정보 등록
            elif cnt == 1:
                fireballs.append([y,x]+world[y][x].pop())
print(sum(i[2] for i in fireballs))




