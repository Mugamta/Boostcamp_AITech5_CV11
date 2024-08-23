'''
메모리 : 31120KB
시간 : 80ms
'''

def main():
    
    N = int(input())
    packs = list(map(int, input().split()))

    '''
    카드 2(인덱스 1)개를 살 수 있는 최저비용부터 dp를 이용하여 업데이트
    
    예시)
    카드 5개 최저 비용 = min( 카드 1개 최저비용 + 카드 4개 최저비용,
                          카드 2개 최저비용 + 카드 3개 최저비용,
                          ------------------------------>> 이하 중복 연산 불필요
                          카드 3개 최저비용 + 카드 2개 최저비용,
                          카드 4개 최저비용 + 카드 1개 최저비용,
    '''
    for i in range(1, N):
        for t in range(0, (i+1)//2):
            packs[i] = min(packs[t]+packs[i-t-1], packs[i])   
    print(packs[-1])    
    

if __name__=="__main__":
    main()