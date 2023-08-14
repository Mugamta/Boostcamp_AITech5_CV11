import sys 

#11퍼센트에서 틀림


T = int(input()) #Test 개수 T
arr = []
for _ in range(T) :
    N = int(input()) # 배열의 길이 N
    A = list(map(int, sys.stdin.readline().split())) #배열
    
    plus = 0
    minus = 0
    
    
    if A[0] > 0 :
        tt = True
        plus += 1
    
    else : 
        tt = False 
        minus += 1

    temp = A[0]

    if sum(A) > 0 : 
        print("YES")
    else :
        for i in range(1,N) :
            if tt : #이전에 양수였으면
                if A[i] > 0 : #양수->양수
                    temp = A[i]
                    plus += 1
                else : #양수->음수
                    if temp + A[i] > 0 : #더했는데 양수
                        temp += A[i]
                        tt = True
                    elif temp + A[i] < 0 : #더했는데 음수
                        temp = A[i] 
                        minus += 1
                        tt = False


            else : #이전에 음수였으면 
                if A[i]<0 : #음수->음수
                    temp += A[i]
                else : #음수->양수
                    if temp + A[i] < 0 : #더했는데 음수
                        temp = A[i]
                        plus += 1
                        tt = True
                    elif temp + A[i] > 0 : #더했는데 양수 
                        minus -= 1
                        plus += 1
                        temp += A[i]
                        tt = True
        print(f"plus = {plus}, minus ={minus}")
        if plus > minus :
            print("YES")
        else : print("NO")