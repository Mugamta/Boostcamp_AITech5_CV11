# time: 1hr 05m
from itertools import combinations, permutations
from collections import Counter, defaultdict

def solution(dice):
    """
    goal: 자신이 승리할 확률이 가장 높아지기 위해 A가 골라야 하는 주사위 번호를 '오름차순으로' 1차원 정수 배열에 담아 반환
    note:
        - A와 B가 n개의 주사위를 가지고 승부
        - 주사위의 6개 면에 각각 하나의 수가 쓰여 있으며, 각 면이 나올 확률을 동일
        - 각 주사위는 '1 ~ n'의 번호를 가지며, 주사위에 쓰인 수의 구성은 '모두 다름'
        - A가 먼저 n / 2 개의 주사위를 가져가면 B가 남은 n / 2 개의 주사위를 가져감
        - 각각 가져간 주사위를 '모두 굴린 뒤', 나온 수들을 모두 합해 점수를 계산 (점수가 같으면 무승부)
    args:
        - dice: 주사위에 쓰인 수의 구성을 담은 2차원 배열
    how:
        - 브루트 포스
        - 10개의 주사위(최대)가 주어졌을 때 뽑을 수 있는 조합은 10C5. 대략 250개
        - 5개 주사위를 던져서 나올 수 있는 경우의 수는 6**5. 32 * 243으로 대략 6만개
        - 주사위 굴린 결과의 시간복잡도는 최악일 때 수천만 정도
        - A와 B 결과 간 비교 연산을 최적화해야함 (중복되는 비교를 최소화) -> Counter 사용
    """
    # A와 B가 가져갈 수 있는 주사위 조합 구하기
    n_dice = len(dice)
    a_combs = list(combinations([i for i in range(n_dice)], n_dice // 2))
    b_combs = [tuple(set(i for i in range(n_dice)) - set(a_comb)) for a_comb in a_combs]
    
    # 주사위 구성 간소화하기
    dice = [list(Counter(setting).items())for setting in dice]
    
    # A와 B가 고른 주사위를 굴려서 나올 수 있는 모든 경우의 수 계산하기
    def simulation(combs):
        nonlocal dice
        
        def dfs(comb, dice_idx=0):
            # stack에 고른 주사위만큼 차면, 합과 등장횟수를 계산해서 simul_res에 추가하기
            nonlocal stack
            if len(stack) == len(comb):
                sum_res, freq = 0, 1
                for num, cnt in stack:
                    sum_res += num
                    freq *= cnt
                    
                nonlocal simul_res
                simul[sum_res] += freq
                return
            
            # 예외처리
            if dice_idx >= len(comb):
                return
            
            # stack 채우기 (값, 등장횟수)
            for val in dice[comb[dice_idx]]:
                stack.append(val)
                dfs(comb, dice_idx + 1)
                stack.pop()
        
        simul_res = []
        for comb in combs:
            simul = defaultdict(int)
            stack = []
            dfs(comb)
            
            simul_res.append(list(simul.items()))
        
        return simul_res
    
    simul_a = simulation(a_combs)
    simul_b = simulation(b_combs)
    
    # A와 B의 시뮬레이션 결과를 비교해서 확률 계산하기
    total_simul = []
    for simul_num in range(len(a_combs)):
        win, draw, lose = 0, 0, 0
        for sum_a, cnt_a in simul_a[simul_num]:
            for sum_b, cnt_b in simul_b[simul_num]:
                if sum_a > sum_b:
                    win += (cnt_a * cnt_b)
                elif sum_a == sum_b:
                    draw += (cnt_a * cnt_b)
                elif sum_a < sum_b:
                    lose += (cnt_a * cnt_b)

        total_simul.append((simul_num, win / (win + draw + lose)))
    
    # 승률이 가장 높은 조합 찾기
    comb_num, _ = max(total_simul, key=lambda x: x[1])
    
    return [dice_idx + 1 for dice_idx in a_combs[comb_num]]
    