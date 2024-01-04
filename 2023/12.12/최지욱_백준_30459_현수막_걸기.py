def main():
    
    n,m,r = map(int, input().split())
    arr = list(map(int, input().split()))
    poles = list(map(int, input().split()))
    
    poles.sort(reverse=True)    ## 깃대는 긴 순으로 정렬
    
    lengths = set()     ## 말뚝 간 길이
    
    for i in range(n):  ## 말뚝 간 길이 가능한 모든 조합 탐색
        for t in range(i+1, n):
            lengths.add(abs(arr[t]-arr[i]))
    
    MAX= -1
    
    lengths = list(lengths)
    lengths.sort()              ## 길이는 짧은 순으로 정렬
    
    index = 0
    for pole in poles:          ## 긴 깃대부터
        while index<len(lengths):
            s = round(pole* lengths[index] *0.5,1)      ## 넓이 구하는 식
            if s<= r:   ## 넓이가 제한치보다 작은 경우 MAX 넓이 업데이트
                MAX = max(s, MAX)
                index += 1          ## 다음 length
            else:       ## 넓이가 제한치보다 커지면 break(더 긴 길이 탐색 불필요)
                break
            
    print(MAX)
    
    return 0


if __name__ == '__main__':
    main()