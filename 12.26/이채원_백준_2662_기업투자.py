import sys

N, M = map(int, sys.stdin.readline().split()) #투자 액수 N, 기업 개수 M
arr = [[0]*(M+1)]
for i in range(N) :
    arr.append(list(map(int, sys.stdin.readline().split())))           
# print(arr)
dp = list( [0]*(M+1) for _ in range(N)) #[A, B, 이익] dp 배열 생성
# print(dp)

# #dp[0]
first_arr = arr[1][1:]
mx = max(first_arr)
index = first_arr.index(mx)

dp[0][-1] = mx
dp[0][index] = 1
# print(dp[0])

temp = list([0]*(M+1) for _ in range(2*M))
for i in range(1, N) :
    for j in range(M) : 
        temp[j] = dp[i-1].copy()
        temp[j][j] += 1
        temp[j][-1]=0
        for k in range(M) :
            temp[j][-1] += arr[temp[j][k]][k+1]
        
    for j in range(M) :
        temp[M+j] = [0]*(M+1)
        temp[M+j][j] = i+1
        temp[M+j][-1] = arr[i+1][j+1]
    
    ben = list(temp[i][-1] for i in range(2*M))
    mx = max(ben)
    index = ben.index(mx)

    dp[i] = temp[index].copy()
    print(f"i={i}, mx={mx}")
    print("temp")
    print(temp)
    print(dp[i])
print(dp[-1][2])
print(dp[-1][0], dp[-1][1])