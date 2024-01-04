import sys

N = int(input())
S = []
for _ in range(N) :
    S.append(input())

temp = [[],[]]
for i in range(N) :
    temp[i%2] = []
    if len(S[i]) == 1  :
        if S[i] not in temp[(i+1)%2] :
            temp[i%2].append(S[i])
    else :        
        for j in range(len(S[i])) :
            s = S[i][len(S[i])-j-1:]
            if s not in temp[(i+1)%2] :
                temp[i%2].append(s)
        # for k in range(len)        
            # print(f"word = {S[i]}, s={s}, temp={temp}")
print(len(temp[(N+1)%2]))

    


    