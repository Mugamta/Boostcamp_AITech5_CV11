#시간초과

import sys
N = int(input())

arr = list(False for _ in range(N))
answer = []
temp = 0

for i in range(N) :
    for j in range(N) :
        if arr[j] == False :
            num = temp + j + 1
            nn = 0

            #소수 검증
            for k in range(num) :
                if num%(k+1) == 0 :
                    nn += 1
                        

            if nn != 2 and nn != 1 : #소수가 아닐때
                answer.append(str(j+1))
                arr[j] = True
                temp += j+1
                break

            else : #소수일때
                pass

if len(answer)==N : 
    print ("YES")
    print(' '.join(answer))
else :
    print("NO")
    # print(answer)