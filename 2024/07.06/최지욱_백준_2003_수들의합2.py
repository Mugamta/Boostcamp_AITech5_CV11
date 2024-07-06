'''
시간 : 44ms
메모리 : 32140ms
'''


def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    head, tail = 0, 0 
    SUM = arr[0]
    cnt = 0
    
    while tail < N and head <= tail:
        if SUM == M:
            cnt += 1
            tail += 1
            if tail < N:
                SUM += arr[tail]
        elif SUM > M:
            SUM -= arr[head]
            head += 1
        else: 
            tail += 1
            if tail < N:
                SUM += arr[tail]
            
    print(cnt)
   
if __name__ == '__main__':
    main()
