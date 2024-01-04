def flip(a, op):                ## 뒤집기 함수
    result = ''
    for i in range(9):
        if op[i]==1:
            if a[i]=='H':
                result += 'T'
            else:
                result += 'H'
        else:
            result += a[i]
        
    return result
        
def main():
    
    cnt = dict()                ## 뒤집는 횟수 저장 dictionary  {case : flip count}      
    
    cnt['HHHHHHHHH'] = 0        ## 전부 앞 혹은 뒤로 시작
    cnt['TTTTTTTTT'] = 0
    
    ops = [(1,1,1,0,0,0,0,0,0), ## ops : 뒤집는 방법 정의
           (0,0,0,1,1,1,0,0,0),
           (0,0,0,0,0,0,1,1,1),
           (1,0,0,1,0,0,1,0,0),
           (0,1,0,0,1,0,0,1,0),
           (0,0,1,0,0,1,0,0,1),
           (0,0,1,0,1,0,1,0,0),
           (1,0,0,0,1,0,0,0,1)]
    
    for _ in range(6):          ## 6회 이내
        cases = list(cnt.keys()).copy()
        
        for case in cases:      ## case들에 대해
            num = cnt[case]
            
            for op in ops:      ## case에 대해 뒤집어보기
                new_case = flip(case, op)
                if new_case not in cnt:     ## 새로운 case인 경우 횟수 설정
                    cnt[new_case] = num+1

    n = int(input())
    
    for _ in range(n):
        string = (input()+ input() + input()).replace(' ','')
        print(cnt[string]) if string in cnt else print(-1)  ## 경우의 수에 대해 flip 횟수 탐색
          
    return 0


if __name__ == '__main__':
    main()