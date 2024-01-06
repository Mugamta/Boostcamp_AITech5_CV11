import sys

N = int(input()) #숙제의 개수 N
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
arr.sort( key=lambda x : [-x[1] ,x[0]])
# print(arr)

done = list(False for _ in range(N))
answer = 0
index = 0

for i in range(N) :
    dead, num = arr[i]
    if index<dead :
        answer += num 
        index = dead
        done[dead-1] = True
    else :
        for j in range(dead) :
            if done[dead-1-j] == False :
                answer += num 
                done[dead-1-j] = True
                break

print(answer)

