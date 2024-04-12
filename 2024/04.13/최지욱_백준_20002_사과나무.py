def main():
    
    N = int(input())
    arr= []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    
    
    ## 누적합을 이용하여 연산의 중복을 막을 수 있음
    ## 4개 지점의 누적합을 이용하여 모든 사각형의 내부 이익 연산 가능
    ## square[r-k, c-k ~ r, k] = arr[r][c] - arr[r-k][c] - arr[r][c-k] + arr[r-k][c-k]
    for r in range(N):
        for c in range(N-1):
            arr[r][c+1] += arr[r][c]

    for c in range(N):
        for r in range(N-1):
            arr[r+1][c] += arr[r][c]
    
    
    ## 연산의 편의를 위해 최상단행과 최좌측열에 zero padding 적용
    arr = [[0 for _ in range(N)]] + arr
    for i in range(N+1):
        arr[i] = [0] + arr[i]
    
    
    ## 정사각형의 크기 k에 따른 모든 정사각형 내부 이익 계산
    MAX = -1000
    for k in range(1, N+1):
        for r in range(k, N+1):
            for c in range(k, N+1):
                MAX = max(MAX, arr[r][c]-arr[r-k][c]-arr[r][c-k]+arr[r-k][c-k])
    
    
    print(MAX)
    return 0


if __name__ == '__main__':
    main()
    
    