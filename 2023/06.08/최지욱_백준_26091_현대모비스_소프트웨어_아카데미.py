from collections import deque

def main():
    
    N, M = map(int, input().split())
    arr = list(map(int, input().split())) 
    arr.sort()
    
    if len(arr)<2:      ## 2명 미만이면 팀 구성 불가, 0을 return 
        print(0)
        return 0
    
    arr = deque(arr)
    MIN = arr.popleft() 
    MAX = arr.pop()
    total = int((MIN+MAX)>=M)       ## 최소+최대 가 M보다 크면 팀 구성가능(+1)
    while arr:
        if MIN+MAX<M:
            MIN = arr.popleft()     ## M보다 작으면 MIN 값만 업데이트 
        else:                       ## M보다 같거나 크면(팀을 구성할 수 있을 때)
            MIN = arr.popleft()     ## MIN
            if arr:
                MAX = arr.pop()     ## MAX
            else:
                break
            total += 1              ## 최소+최대 가 M보다 크면 팀 구성가능(+1)
            
    print(total)
    
    
main()