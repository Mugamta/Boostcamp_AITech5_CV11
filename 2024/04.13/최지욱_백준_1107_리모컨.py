def main():
    
    N = int(input())
    M = int(input())
    
    if M:
        ban = list(input().split())
    else:
        ban = []
    
    ## 희망 채널로부터 N-1, N-2, N-3 ..., N+1, N+2, N+3 ... 로 진행하며
    ## 가능한 채널인지 여부를 확인. 
    ## 가능한 경우 진행한 버튼수(cnt)와 채널의 숫자길이(len(channel))의 합이 버튼 수
    up = N
    down = N
    cnt =0
    
    ## 최소 버튼 수를 구하기 위한 후보 리스트
    candidate= [abs(N-100)]
    
    ## 최소 N-100만큼은 반복
    for i in range(abs(N-100)):
        
        ## 아래쪽 가능한 수인지 판별
        BOTTOM = True
        for num in str(down):
            if num in ban:
                BOTTOM = False
                break
        ## 가능하면 버튼수 후보군으로 추가
        if BOTTOM:
            candidate.append(len(str(down))+cnt)
        
        
        ## 위쪽 가능한 수인지 판별
        TOP = True
        for num in str(up):
            if num in ban:
                TOP = False
                break
        ## 가능하면 버튼수 후보군으로 추가
        if TOP:
            candidate.append(len(str(up))+cnt)

        
        ## 가능한 경우의 수를 찾아낸 경우 가장 최소의 버튼수로 반환
        if TOP or BOTTOM:
            print(min(candidate))
            return
        
        up += 1
        down -= 1
        cnt +=1

    ## N-100만큼 반복해도 구할 수 없으면 N-100이 최소 버튼 수
    print(abs(N-100))
    return

if __name__ == '__main__':
    main() 