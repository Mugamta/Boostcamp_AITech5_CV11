import sys

def solution():
    N = int(input())
    arr = list(map(int,sys.stdin.readline().split()))
    arr.sort(key= abs, reverse=True)
    temp = 2000000000
  
    for i in range(N-1) :
        # for j in range(i+1, len(arr)) :
        now = abs(arr[i] + arr[i+1])
        if now < temp :            
            temp = now
            answer =[arr[i], arr[i+1]]
        
    
    answer.sort()
    print(answer[0], answer[1]) 

solution()