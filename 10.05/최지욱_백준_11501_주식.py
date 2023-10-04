def main():
    
    T = int(input())
    
    for _ in range(T):
        
        N = int(input())
        arr = list(map(int, input().split()))
        MAX = 0
        SUM = 0
        
        while arr:
            target = arr.pop()
            
            if target > MAX:
                MAX = target
            else:
                SUM += MAX-target
        
        print(SUM)

main()