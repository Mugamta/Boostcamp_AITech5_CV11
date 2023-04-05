# 11:20 시작
# 11:25 wanho, score 정렬 및 탐색 생각
# 11:33 wanho보다 순위가 높은 사람이 나올 때 마다 wanho의 순위를 1씩 낮추도록 구현
# 11:38 테스트케이스 실패
# 11:42 15줄의 비교 연산에서 동료 평가 점수가 같은 사람 추가하여 해결


def solution(scores):
    wanho = scores.pop(0)
    scores.sort(key=lambda x:(-x[0],x[1]))
    temp = 0
    answer = 1
    for i,j in scores:
        if wanho[0]<i and  wanho[1]<j:
            return -1
        if temp <= j:
            temp = j
            if wanho[0]+wanho[1] < i + j:
                answer += 1
    return answer