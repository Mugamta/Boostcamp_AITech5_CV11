# 11시 20분 시작
# 11시 24분 lenth 구현
# 11시 32분 테케통과
# 11시 34분 제출 실패 -> 시간초과 10개 -> sum 과정에서 시간단축 필요
# 11시 38분 제출 실패 -> 시간초과 4개 -> pop deque 사용해야함
# 11시 40분 제출 성공!!
from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    a = sum(queue1)
    b = sum(queue2)
    lenth = 4*len(queue1)
    answer = 0
    while a != b:
        if a > b:
            a1 = q1.popleft()
            q2.append(a1)
            b += a1
            a -= a1
        else:
            b1 = q2.popleft()
            q1.append(b1)
            a += b1
            b -= b1
        answer += 1
        # a = sum(queue1)
        # b = sum(queue2)
        if answer > lenth:
            return -1
    return answer