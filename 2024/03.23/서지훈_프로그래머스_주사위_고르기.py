# 참조
# https://school.programmers.co.kr/questions/74109
# https://tech.kakao.com/2023/12/27/2024-coding-test-winter-internship/
from itertools import combinations

def solution(dice):
    answer = []
    
    n = len(dice)
    
    # 주사위를 고르는 방법 - 최대 C(10, 5) = 252 - C(n, n / 2)
    
    li = [i for i in range(n)]
    
    # combinations는 iterable에서 주어진 길이만큼의 조합을 만들어 tuple 반환
    comb = list(combinations(li, n // 2))
    
    # 이 값은 오름차순이므로, 첫 값과 마지막 값, 두번째 값과 마지막 값의 앞의 값...이 A, B의 선택이 됨
    # 이를 리스트로 만들면 아래와 같음
    select = [[comb[i], comb[len(comb) - 1 - i]] for i in range(len(comb)//2)]
    
    # 핵심은 n^(n / 2)의 경우의 수를 가질 수 있는, 주사위의 수...
    # 이를 효율적으로 개선할 수 있는 방법이 필요
    
    # 이를 위해 이미 존재하는 값을 카운팅함
    # 가령, [1, 2, 3]에서 [1, 2, 3], [1, 2, 3]을 뽑는 경우
    # 앞의 두 주사위의 경우 2가 한 번, 3이 두 번...의 형식으로 중복된 값들이 존재함
    # 이를 모두 고려하면 n^(n / 2)가 되지만, 이를 카운팅하여 활용하면 주사위의 값인 100^2 * 5 이내로 단축 가능
    
    max_win = 0
    # A, B의 주사위 선택
    for A, B in select:
        
        # 최대 값인 100까지를 담는 리스트를 사용할 수 있으나, 이 경우 존재하는 값을 일일히 찾아야 함
        # 따라서 dict 사용이 효율적
        valueA = dict()
        
        # 첫 번째 주사위는 우선 넣음
        for value in dice[A[0]]:
            if value not in valueA:
                valueA[value] = 1
            else:
                valueA[value] += 1
        
        # 이후 주사위부터 순회
        for i in range(1, n // 2):
            tmp = dict()  # 새로운 딕셔너리를 생성 (기존 기댓값을 버려야 하므로)

            # 현재 저장된 가능한 주사위 값을 불러옴
            for before_case in valueA.keys():
                for num in dice[A[i]]:  # 그리고 선택한 주사위의 값을 불러옴
                    # 이 두 주사위의 합에 기댓값을 저장하거나 더함
                    if before_case + num not in tmp:
                        tmp[before_case+num] = valueA[before_case]
                    else:
                        tmp[before_case+num] += valueA[before_case]
                        
            # 그리고 기존 기댓값을 버리기 위하여 덮어씌움
            valueA = tmp
        
        
        # B의 경우도 동일한 로직
        valueB = dict()
        
        for value in dice[B[0]]:
            if value not in valueB:
                valueB[value] = 1
            else:
                valueB[value] += 1
        
        for i in range(1, n // 2):
            tmp = dict()

            for before_case in valueB.keys():
                for num in dice[B[i]]:
                    if before_case + num not in tmp:
                        tmp[before_case+num] = valueB[before_case]
                    else:
                        tmp[before_case+num] += valueB[before_case]
            valueB = tmp
        
        
        # 이제 A, B가 가져가는 주사위의 기댓값이 구해졌고, 이 값들의 길이는은 각각 500을 넘지 않음
        # (n은 최대 10이며, 주사위의 값은 100 이하이므로)
        # 따라서 이들을 이중 for문으로 순회하여도 250000으로 시간에 문제 없음
        
        valueA_keys = valueA.keys()
        valueB_keys = valueB.keys()  # B의 키는 A의 길이만큼 호출되어야 하므로 저장

        # 승리, 패배, 무승부의 횟수를 각각 저장함
        win, draw, loss = 0, 0, 0
        for a in valueA_keys:
            for b in valueB_keys:
                # 승, 패, 무를 각각 기록
                if a > b:
                    win += valueA[a] * valueB[b]
                elif a == b:
                    draw += valueA[a] * valueB[b]
                else:
                    loss += valueA[a] * valueB[b]

        # 승리할 확률 = 승리하는 경우의 수 / 전체 경우의 수 (무승부 미포함)
        # 전체 경우의 수는 항상 일정하므로, 승리하는 경우의 수만 고려해도 됨
        
        # 따라서 최대 승리의 경우의 수인 경우 A의 선택을 answer에 저장
        if max_win < win:
            max_win = win
            answer = [x + 1 for x in A]
        if max_win < loss:
            max_win = loss
            answer = [x + 1 for x in B]
        
        
    return answer