import sys

N = int(input())
p = [] 
for _ in range(N) :
    P, Q =  map(int, sys.stdin.readline().split())
    p.append([P,Q])
p.sort(key=lambda x : x[0])
ans = list([0, 0] for _ in range(N)) #num, time


for [P, Q] in p :    
    for i in range(N) :
        if ans[i][1] < P : 
            ans[i][0] += 1
            ans[i][1] = Q 
            break

answer = 0
arr = []
for n, t in ans :
    if n != 0 : 
        answer += 1
        arr.append(str(n))
    else : 
        break
print(answer)
print(' '.join(arr))
            

        
