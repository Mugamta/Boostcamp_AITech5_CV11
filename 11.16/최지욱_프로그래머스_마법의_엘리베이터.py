def solution(storey):
    power = 1
    total = 0
    while storey:       ## 층이 0이 될 때까지
        target = (storey % (10**power)) // 10**(power-1)        ## n의 자리수(1, 10,100)
        if target < 5:                      ## 5보다 작으면
            total += target                 ## 내려가는 만큼 마법의 돌 소모
            storey -= target*(10**(power-1))    ## 내려가기
        elif target ==5 and (storey % (10**(power+1))) // 10**(power)<5:    ## 5이면서 그 앞자리수가 5 미만이면
            total += target                                                 ## 내려가는 만큼 마법의 돌 소모
            storey -= target *(10**(power-1))                               ## 내려가기
        else:                                                   ## 이 외의 경우
            total += (10-(target))                              ## 올라가는 만큼 마법의 돌 소모
            storey += (10-(target)) *(10**(power-1))            ## 올라가기
        
        power +=1       ## 자리 수 증가 
    
    return total