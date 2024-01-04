def main():
    
    n = int(input())
    
    arr = list(map(int ,input().split()))
    
    MAX = arr.pop()
    
    while arr:
        target = arr.pop()
        MAX = (((MAX-1) // target) + 1) * target

    print(MAX)
    
main()