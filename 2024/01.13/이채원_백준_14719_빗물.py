import sys

H, W = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
arr = list(int(x) for x in arr)

answer = 0
l_mx = 0
r_mx = 0



for i in range(1, W-1) : #양 끝엔 물이 고일 수 없다. 
    l_mx = max(arr[:i])
    r_mx = max(arr[i+1:])

    idx = min([l_mx, r_mx])
    if arr[i] < idx :
        answer += (idx - arr[i])
print(answer)      
