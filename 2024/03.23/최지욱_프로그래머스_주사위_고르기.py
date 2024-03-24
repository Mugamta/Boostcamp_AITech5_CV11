def solution(dice):
    
    ## cases : 주사위를 선택하는 조합
    length = len(dice)
    cases = [[i] for i in range(length)]
    for _ in range((length//2)-1):
        
        arr=[]
        while cases:
            case = cases.pop()
            for i in range(case[-1]+1, length):
                arr.append(case+[i])
        cases=arr
    
    MAX_WIN = 0
    for index, case in enumerate(cases):
        
        ## A가 선택 후, B가 갖는 주사위 선택 조합
        opp =[]
        for i in range(length):
            if i not in case:
                opp.append(i)
            
        case_scores = [0]
        opp_scores =[0]
        
        ## A의 주사위 선택에 따른 가능한 점수 조합 
        for num in case:
            arr=[]
            while case_scores:
                s = case_scores.pop()
                for score in dice[num]:
                    arr.append(s+score)
            case_scores =arr
        
        ## 나머지 B의 주사위에 따른 가능한 점수 조합
        for num in opp:
            arr=[]
            while opp_scores:
                s = opp_scores.pop()
                for score in dice[num]:
                    arr.append(s+score)
            opp_scores =arr
        
        case_scores.sort()
        opp_scores.sort()
        
        ## 승리하는 경우의 수
        wins = 0
        i, j = 0, 0
        while i < len(case_scores) and j < len(opp_scores):
            if case_scores[i] > opp_scores[j]:
                wins += len(case_scores) - i
                j += 1
            else:
                i += 1
        
        if wins>MAX_WIN:
            MAX_WIN = wins
            max_index = index
    
    ## 최다승 경우의 조합을 return
    return [i+1 for i in cases[max_index]]