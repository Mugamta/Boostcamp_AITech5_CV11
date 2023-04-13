def solution(n, m, x, y, r, c, k):
    
    x_move, y_move = r-x , c-y              ## x,y 방향으로 이동해야 하는 벡터(최단 이동)
    extra = k - abs(x_move) - abs(y_move)   ## 최단으로 이동해야하는 것 이외 움직일 수 있는 extra move

    x-=1
    y-=1
    
    allowed = {'d':max(0, x_move),'l':-min(0, y_move),'u':-min(0, x_move),'r':max(0, y_move)}   ## 방향별 이동가능한 횟수를 사전 정의
    dirs  = {'d':[1,0],'l':[0,-1],'r':[0,1],'u':[-1,0]}             ## 방향 정의
    
    pair ={'l':'r','r':'l','u':'d','d':'u'}     ## 대응하는 이동
    
    arr =[]
    
    for _ in range(k):      ## k번 이동

        for dire in dirs:
            
            if 0<=(x+dirs[dire][0])<n and 0<=(y+dirs[dire][1])<m:       ## 구간체크    
                pass
            else:
                continue
                
            if allowed[dire]>0:         ## 해당하는 방향이 이동 가능한 횟수가 남아있을때
                allowed[dire]-=1        ## 이동 가능한 횟수를 update(-1) 후 이동
                x += dirs[dire][0]
                y += dirs[dire][1]
                arr.append(dire)        ## 이동한 방향 append
                break
            elif extra>0:               ## 해당하는 방향이 이동 가능한 횟수가 남아있을때
                extra -= 2              ## 현재 이동 및 대응(복귀)하는 이동을 차감
                allowed[pair[dire]] += 1  ## 대응하는 방향으로의 이동 가능 횟수 +1
                x += dirs[dire][0]      
                y += dirs[dire][1]
                arr.append(dire)        ## 이동한 방향 append
                break
            else:
                continue
                
    if (x+1,y+1)==(r,c):
        return ''.join(arr)
    else:
        return 'impossible'