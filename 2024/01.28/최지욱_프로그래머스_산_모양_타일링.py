def solution(n, tops):
    arr= [1,1]
    for top in tops:
        if top==1:      ## 위의 삼각형이 있을 때
            arr.append((arr[-2]+2*arr[-1])%10007)
            arr.append((arr[-2]+arr[-1])%10007)
        else:           ## 위의 삼각형이 없을 때 
            arr.append((arr[-2]+arr[-1])%10007)
            arr.append((arr[-2]+arr[-1])%10007)
            
    return arr[-1]