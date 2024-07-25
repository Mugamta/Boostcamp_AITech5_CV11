"""
    - 메모리 : 31120 KB
    - 시  간 : 40 MS

    - 풀이

        전체 작은 정육면체의 보이는 면 갯수 (큰 정육면체를 이루는 작은 정육면체 수)
        -> n**2 * 5 -> 맨 밑의 면은 안보임
        
        i) 이때 3 면이 보이는 작은 정육면체의 갯수
        : 무조건 4-> 맨위의 꼭짓점

        ii) 2 면이 보이는 작은 정육면체의 갯수
        : N = 2 ~> 4개
        : N = 3 ~> 12개

        2a - b = 4
        3a - b = 12 
        > a = 8
        > b = 12 
        : 점화식 : 8N - 12 

        iii) 1 면만 보이는 경우 
        위 경우의 작은 정육면체 모두 더한걸 전체 작은 정육면체 갯수에 빼주면된다 


        이제 3면에 보일때의 최솟값, 2면이 보일때 최솟값 1면에 보일때 최솟값을 구해주면된다
        
        일단 주사위를 접어보자

            A - F
            E - B
            D - C 바라보게 된다
        해당 방법으로 짝을 지으면

        (A,F), (B,E), (C,D) -> 각각의 min 값으로 3가지 값을 구성할 수 있다.
        
        구성할 수 있는 수 = [min(A,F), min(B,E), min(C,D)]

        i) 1 면이 보일때 최솟값
        :min(구성할 수 있는 수)

        ii) 2 면이 보일때 최솟값
        :가장 낮은 구성할 수 있는 수 + 2번째로 낮은 수

        iii) 3면이 보일 때 최솟값
        :sum(구성할 수 있는 수)
"""

import sys
input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))
# 전체 보이는 면의 수
total_square = (N**2) * 5

if N == 1:
    print(sum(dice) - max(dice))
else:
    result = 0
    can_num = []
    for i in range(3):
        can_num.append(min(dice[i], dice[-1-i]))
    # 구성가능한 수 정렬
    can_num.sort()

    # i) 3면이 보이는 경우
    result += (4 * sum(can_num))
    total_square -= (4 * 3) # 4개 * 3면

    # ii) 2면이 보이는 경우
    two_case = (8 * N - 12)
    result += (two_case * sum(can_num[:2]))
    total_square -= (two_case * 2) # 2면이 보이는 경우 갯수 * 2면

    # iii) 1면이 보이는 경우
    result += (total_square * can_num[0])
    print(result)
