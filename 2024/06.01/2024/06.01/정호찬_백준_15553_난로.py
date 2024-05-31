"""
구사과씨 방에는 난로가 있음

혼자 있을때는 되도록 켜지 않음
하지만 2명일때(친구가 오면)난로는 켜져야함

N명의 친구가 오는데 T_i 시간에 와서 T_i+1 시간에 나간다
방이 좁기 떄문에 한번에 한명만 올 수 있으며, 친구가 오는 시간이 겹치지 않음

난로는 언제든지 켤 수 있지만, 한번 킬때 성냥 1개를 소모해야한다
구사과씨는 총 K개의 성냥을 갖고 있다. 

처음에는 난로가 꺼져있음

우리의 목표는 난로가 켜져있는 시간을 최소로 해야함 

예제 1 )
    친구가 3명오고 성냥이 2개있음 (2번킬 수 있음)
    1, 3, 6 시간에 온다
    처음 1에 난로를 키고 -> 두번째 친구가 나간시간(4)에 끈다 
    세번째 친구가 6에 난로를 키고 -> 나가는 시간 7에 끈다

    즉, (4 - 1) + (7 - 6) = 총 4 동안 난로가 켜짐

    핵심은 : 
    성냥이 친구수 보다 적을 경우 연속되는 방문 시간대 차이가 적을떄 
    연속해서 켜져있어야한다 (연속해서 켜져있을 구간을 정해야함)

    성냥의 갯수가 친구와 같거나 많을 경우 최소시간은 친구 수 
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

diff = []
start = int(input())

# 각 시간대의 차이를 저장
for _ in range(N-1):
    now = int(input())
    diff.append(now - start)
    start = now

#성냥 갯수가 친구수 보다 적은 경우
diff.sort()
#가장 시간대 차이를 (K-1)개 제거 (부족한 성냥수 만큼 연속할 시간 남김)
#연속해서 켜져있을 최소 시간을 남김
for _ in range(K-1):
    diff.pop()
#그리고 차이 수의 합 + 성냥 갯수(성냥으로 키고 끌 수 있는 시간은 1 시간+)
print(sum(diff) + K)




