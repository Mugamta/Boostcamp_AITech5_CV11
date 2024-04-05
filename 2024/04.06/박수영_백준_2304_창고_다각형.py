# time: 1hr 16m
import sys
input = sys.stdin.readline

def solution(n, arr):
    """
    goal: 기둥들의 위치와 높이가 주어질 때, '가장 작은 창고 다각형의 면적' 구하기
    note:
        - 창고에는 '모든 기둥'이 들어가며, 기두의 폭은 모두 1m임
        - 지붕은 수평 부분과 수직 부분으로 구성, '모두 연결되어야 함'
        - 지붕의 수평 부분은 '반드시 어떤 기둥의 윗면'과 닿아야 함
        - 지붕의 수직 부분은 '반드시 어떤 기둥의 옆면'과 닿아야 함
        - 지붕의 가장자리는 땅에 닿아야 함
        - 지붕의 어떤 부분도 '오목하게 들어간 부분'이 없어야 함
    how:
        - 큐/스택
        - 지붕 설계에 필요한 기둥만 찾는 방식으로 구현 >> 이는 스택에 저장
    """
    # 왼쪽 면 위치 기준으로 오름차순 정렬
    arr.sort(key=lambda x: x[0])

    stack, tmp = [], []

    # 지붕 설계에 필요한 기둥 찾기
    for l_pos, h in arr:
        if not stack:
            stack.append([l_pos, h])

        else:
            # 높이가 같거나 더 높은 기둥이 등장하면
            # 스택에 값을 추가 및 tmp 초기화
            if stack[-1][1] <= h:
                stack.append([l_pos, h])
                tmp = []

            else:
                # tmp에는 스택의 마지막 기둥보다 높이가 낮은 기둥들을 저장
                if not tmp:
                    tmp.append([l_pos, h])
                
                else:
                    # 새로운 기둥이 tmp의 마지막 기둥보다 높이가 높다면
                    # 오목을 방지하기 위해 tmp의 마지막 기둥을 제거
                    while tmp:
                        if tmp[-1][1] <= h: tmp.pop()
                        else: break

                    tmp.append([l_pos, h])

    # tmp에 남아있는 값을 스택에 추가
    if tmp: stack.extend(tmp)

    # 두 기둥 사이 면적 구하기 (왼쪽 면적 기준)
    min_area = 0
    for i in range(len(stack) - 1):
        l1, h1 = stack[i]
        l2, h2 = stack[i + 1]

        if h2 >= h1:
            min_area += ((h2 * (l2 - l1)) - (h2 - h1) * (l2 - l1))
        else:
            min_area += ((h1 * (l2 - l1)) - ((h1 - h2) * (l2 - (l1 + 1))))

    # 마지막 기둥의 면적을 더함
    min_area += stack[-1][1]

    return min_area


if __name__ == "__main__":
    # 입력
    N = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = solution(N, arr)
    print(res)
