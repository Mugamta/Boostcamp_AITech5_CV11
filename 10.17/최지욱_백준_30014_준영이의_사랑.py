def main():
    
    num = int(input())
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    head = []
    tail = []
    
    turn = True
    
    while arr:
        if turn:
            head.append(arr.pop())
            turn = False
        else:
            tail.append(arr.pop())
            turn = True
            
    arr = head + tail[::-1]
    
    prev = arr[-1]
    SUM = 0
    
    for i in arr:
        SUM += prev*i
        prev = i
        
    print(SUM)
    print(" ".join([str(i) for i in arr]))
    
    
main()