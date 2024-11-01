"""
주사위를 쌓기위해서는 겹치는 면의 숫자가 같아야함
이렇게 쌓아 올라서 하나의 긴 사각 기둥을 만들고 
각 기둥에는 4개의 옆면이 존재
해당 옆면의 한면에 적힌 숫자의 합이 가장큰 수를 구해야함

-> 접근방법
어차피 옆에 위치하는 숫자들 그러니까 위 아래 면에 숫자가 아니라면
이를 회전해서 최대가 될 수 있다

즉, 우리가 해야할 것은 위, 아래 즉, 쌓는 면에 위치하는 숫자들이 최소가 되게 만들어야함

how to 최소로 만들것인가)
브루트 포스로 전체 탐색을 수행해야하는가
어차피 밑면이 정해면 윗면은 자동으로 정해짐
그리고 주사위를 쌓는것은 1 ~ n까지 순서가 정해짐
"""
import sys
input = sys.stdin.readline

def get_max_side_value(dice, bottom, top):
    """주사위의 옆면 중 최대값을 반환"""
    return max(num for i, num in enumerate(dice) if i != bottom and i != top)

def solution(n, dices):
    # 주사위 반대면 매핑
    matches = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
    max_total = 0
    
    # 첫 주사위의 각 면이 바닥이 되는 경우 시도
    for first_bottom in range(6):
        total = 0
        bottom = first_bottom
        
        # 각 주사위마다 옆면의 최대값 계산
        for i in range(n):
            top = matches[bottom]
            total += get_max_side_value(dices[i], bottom, top)
            
            # 다음 주사위를 위한 bottom 인덱스 계산
            if i < (n - 1):
                bottom = dices[i + 1].index(dices[i][top])
        
        max_total = max(max_total, total)
    
    return max_total

# 입력 처리
n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, dices))