

import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

ans = list(False for _ in range(N))

for i in range(N) :
    k = arr[i] #왼쪽의 키큰 사람 수 
    temp = 0
    for j in range(N) :
        if ans[j] == False :
            if temp == k :
                break
            else : temp += 1
        else : 
            pass
        # print(f"i={i+1},j={j},temp={temp},ans={ans}")

    
    ans[j] = str(i+1)

print(' '.join(ans))
