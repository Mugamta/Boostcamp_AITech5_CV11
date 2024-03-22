from itertools import combinations, product
from bisect import bisect_left

def calculate_win(a_c, b_c, dice):
    # make all selections
    A = [sum(p) for p in list(product(*[dice[f] for f in a_c]))]
    B = sorted([sum(p) for p in list(product(*[dice[f] for f in b_c]))])
    
    # win calculate - by binary search
    wins = sum(bisect_left(B, value) for value in A)

    # # win calculate
    # wins = 0
    # for a_i in A:
    #     idx = 0
    #     while (idx < len(B) and a_i > B[idx]):
    #         wins+=1
    #         idx+=1
    #     wins+=idx

    return (wins)

def solution(dice):
    best_result = [[], 0] #index, win
    n = len(dice)
    a_comb = list(combinations(range(n), n // 2))
    for a_c in a_comb:
        b_c = [i for i in range(n) if i not in a_c]
        
        #update
        win_tmp = calculate_win(a_c, b_c, dice)
        if best_result[1] < win_tmp:
            best_result[1] = win_tmp
            best_result[0] = a_c

    return [f+1 for f in best_result[0]]