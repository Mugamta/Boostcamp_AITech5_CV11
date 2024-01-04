# 입력 받기
import sys
input = sys.stdin.readline
# 테스트 케이스 수
n = int(input())
for _ in range(n):
    # 스티커의 열의 수
    r = int(input())
    # 1행 스티커의 점수
    m1 = [0]+list(map(int, input().split()))
    # 2행 스티커의 점수
    m2 = [0]+list(map(int, input().split()))

    # 인덱스가 1일때 최댓값은 이전 대각선의 스티커 점수
    m1[1] += m2[0]
    m2[1] += m1[0]

    # 인덱스가 1 보다 클 때 최댓값은 두칸 전에 스티커 값과 이전 스티커 값 중에서 큰 값과 현재 스티커의 값을 더한 값
    for i in range(2, r+1):
        m1[i] += max(m2[i-1], m2[i-2])
        m2[i] += max(m1[i-1], m1[i-2])

    print(max(m1[r], m2[r]))