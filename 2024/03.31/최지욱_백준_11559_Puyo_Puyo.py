def main():
    
    board = [input() for i in range(12)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    stacks=[]
    for i in range(6):          ## 각 열 별로 뿌요 저장(제거 시 아래로 떨어지도록)
        stacks.append([])
        for j in range(11,-1,-1):
            stacks[i].append(board[j][i])

    cnt = 0         ## 몇 번 반복하는지 측정
    while True:
        
        visited= [[False for _ in range(12)] for _ in range(6)] 
        remove = [] 
        
        for h in range(12):
            for w in range(6):
                if stacks[w][h]!='.' and not visited[w][h]:
                    target = stacks[w][h]
                    visited[w][h] = True
                    
                    locs = [[w,h]]      ## 연결이 되는 위치들
                    for w, h in locs:   
                        for dw, dh in dirs:     ## 조건을 만족하면 연결로 추가
                            if (0<=w+dw<6) and (0<=h+dh<12) and (stacks[w+dw][h+dh]==target) and not visited[w+dw][h+dh]:
                                locs.append([w+dw, h+dh])
                                visited[w+dw][h+dh] = True
                    
                    if len(locs)>3:     ## 연결된 대상이 4개 이상인 경우   
                        remove += locs  ## 제거 대상으로 추가
        
        if not remove:  ## 제거할 대상이 없으면 반복 종료
            break
        
        remove.sort(key=lambda x:x[1], reverse=True)    ## 제거 대상을 정렬(위에서부터 제거)
        
        for w,h in remove:
            stacks[w].pop(h)        ## 위에서 부터 제거 후
            stacks[w].append('.')   ## 위는 .으로 채우기

        cnt += 1
        
    print(cnt)
    return 0


if __name__ == '__main__':
    main()