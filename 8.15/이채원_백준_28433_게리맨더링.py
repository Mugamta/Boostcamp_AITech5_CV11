import sys 

#11퍼센트에서 틀림


T = int(input()) #Test 개수 T

for _ in range(T) :
    N = int(input()) # 배열의 길이 N
    A = list(map(int, sys.stdin.readline().split())) #배열

    if sum(A) > 0  : 
        print("YES")
    elif len(A) == 1 : 
        print('NO')
    else :
        plus = 0
        minus = 0
        
        for i in range(N) :
            if A[i] != 0 :
                temp = A[i]
                t = i
                break
        
        if temp > 0 :
            plus += 1
        
        else : 
            minus += 1

        for i in range(t+1,N) :
            if temp>0 : #이전에 양수였으면
                if A[i] > 0 : #양수->양수
                    temp = A[i]
                    plus += 1
                elif A[i]<0 : #양수->음수
                    if temp + A[i] > 0 : #더했는데 양수
                        temp += A[i]
                      
                    else: #더했는데 음수 또는 0
                        temp = A[i] 
                        minus += 1
                else :  #0이 들어오면
                    temp = 0
                        

                        



            elif temp<0 : #이전에 음수였으면 
                if A[i]<0 : #음수->음수
                    temp += A[i]
                elif A[i]>0 : #음수->양수
                    if temp + A[i] < 0 : #더했는데 음수
                        temp = A[i]
                        plus += 1
                        
                    else : #더했는데 양수 
                        minus -= 1
                        plus += 1
                        temp += A[i]
                else : 
                    temp = 0
                        
            else : #더했는데 0
                temp = A[i]
                if A[i]>0 : 
                    plus += 1
                elif A[i] <0 :
                    minus += 1
                else : 
                    temp = 0
                    
                


        # print(f"plus = {plus}, minus ={minus}")
        if plus > minus :
            print("YES")
        else : print("NO")