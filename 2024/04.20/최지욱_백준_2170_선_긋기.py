import sys

def main():
    
    N = int(input())
    arr = []
    
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    arr.sort()
    
    TOTAL = 0
    MIN = -1000000000
    MAX = -1000000000
    
    for s, e in arr:
        if s<=MAX:
            MAX=max(MAX, e)
        else:
            TOTAL += (MAX-MIN)
            MIN = s
            MAX = e            
            
    print(TOTAL + (MAX-MIN))
    return 0


if __name__ == '__main__':
    main()