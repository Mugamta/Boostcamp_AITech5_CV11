def main():
    n = int(input())
    arr = list(map(int, input().split()))

    prev = 0
    SUM = []        ## 리스트 (index를 종료 지점으로 갖는 가장 큰 값)
    
    for i in arr:
        prev = max(prev+i,0)        ## 이전 최대합에 현재 원소를 더해줌, 최대합이 음수면 0으로
        SUM.append(prev)

    if max(SUM):            ## 가장 큰 합을 출력
        print(max(SUM))    
    else:                   ## 음수만 있을때 max 원소 출력
        print(max(arr))

main()


# 1
# arr : [10, -4, 3,  1,  5,  6, -35, 12, 21, -1]
# SUM : [10,  6, 9, 10, 15, 21,   0, 12, 33, 32]

# 2
# arr : [2, 1, -4, 3, 4, -4, 6,  5, -5,  1]
# SUM : [2, 3,  0, 3, 7,  3, 9, 14,  9, 10]

# 0
# arr : [-1, -2, -3, -4, -5]
# SUM : [ 0,  0,  0,  0,  0]