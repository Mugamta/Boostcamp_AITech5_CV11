'''
02:50 구현 시작

dir 오타 발견

04:00

check_dir 오류 재수정
'''
def main():
    
    N,M,K = list(map(int, input().split(' ')))
    
    balls =[]
    for _ in range(M):
        r,c,m,s,d = list(map(int,input().split(' ')))
        balls.append([r-1,c-1,m,s,d])
        
    dir = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
    
    for _ in range(K):
        new_balls = dict()
        
        ## move balls
        for ball in balls:
            r,c,m,s,d = ball
            r = (r + s*dir[d][1])%N
            c = (c + s*dir[d][0])%N
            loc_string = str(r)+','+str(c)      ## 위치에 따른 ball들을 dictionary에 저장
            if loc_string in new_balls:
                new_balls[loc_string].append([m,s,d])
            else:
                new_balls[loc_string] = [[m,s,d]] 
        
        balls = []
        ## merge and split balls
        for ball in new_balls:
            
            if len(new_balls[ball])==1:                     ## 1개이면 그대로 다음 balls에 append
                r,c = list(map(int, ball.split(',')))
                m,s,d = new_balls[ball][0]
                balls.append([r,c,m,s,d])
            else:
                r,c = list(map(int, ball.split(',')))       ## 2개 이상인 경우 merge
                post_m, post_s = 0,0
                check_dir =[]
                
                for m,s,d in new_balls[ball]:         ## merge 대상 fireball들의 속성들을 취합  
                    post_m += m 
                    post_s += s
                    check_dir.append(d%2)             ## to set next directions
                
                post_m = post_m //5
                post_s = post_s //len(new_balls[ball])
                
                if post_m==0:                           ## 질량 0인 경우 삭제
                    continue
                else:
                    if 0 not in check_dir or 1 not in check_dir:    ## 나머지가 0,1이 들어가지 않은경우(0 또는 1로만 이루어진 경우)
                        balls.append([r,c,post_m,post_s,0])
                        balls.append([r,c,post_m,post_s,2])
                        balls.append([r,c,post_m,post_s,4])
                        balls.append([r,c,post_m,post_s,6])
                    else:                                           ## 나머지 0,1이 섞인 경우
                        balls.append([r,c,post_m,post_s,1])
                        balls.append([r,c,post_m,post_s,3])
                        balls.append([r,c,post_m,post_s,5])
                        balls.append([r,c,post_m,post_s,7])
                    
     
    print(sum([ball[2] for ball in balls]))     
        
main()