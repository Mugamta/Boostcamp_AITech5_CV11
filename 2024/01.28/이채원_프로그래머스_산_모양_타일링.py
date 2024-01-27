def solution(n, tops):
    arr = list(0 for _ in range(n+1))
    arr[0] = 1 #계산상 필요에 의해 추가
    
    if tops[0] == 0 :   #맨 처음 노드는 먼저 계산
        arr[1] = 3
    else : 
        arr[1] = 4
        
    for i in range(1,n) :
        if tops[i] == 0 : #위에 삼각형 뿔이 붙지 않았을 경우
            arr[i+1] = (arr[i] - arr[i-1]) * 3 + arr[i-1] * 2
        else : #위에 삼각형 뿔이 붙었을 경우
            arr[i+1] = (arr[i] - arr[i-1]) * 4 + arr[i-1] * 3
        
    return arr[-1] % 10007