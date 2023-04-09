# 1:25 시작
# Fn = Fn-1 + Fn-2 (n ≥ 2)
# 1:27 공식대로 재귀함수 구현
# 작은 수는 가능하지만 큰수는 RecursionError
# 1:30 다른 방법 생각 시작
# 100만으로 나눈 나머지를 구하는 방법
# 힌트 주신 것 기반으로 동적 계획법 이외의 방법 생각
# 합,곱,제곱,차,몫,나머지 시도
# 3:00 피보나치 큰수 검색
# 피보나치 수열의 합, 홀수항의 합, 짝수항의 합, 제곱의 합, 분수의 합
# 3:37 피사노 주기 !!! N 번째 피보나치 수를 (나누는 수)로 나눈 나머지는 (N % 주기) 번째 수를 (나누는 수)로 나눈 나머지와 같다.
# 나누는 수 = 10**(K) 일때, 주기 = 15*10(K-1)
# 8:30 재시작
# 8:46 제출

import sys
input = sys.stdin.readline
n = int(input())

def fre(num):
    k = len(str(num))-1
    return 15*(10**(k-1))

def cal(n,num):
    f = fre(num)
    dp = [0]*f
    for i in range(f):
        if i < 2:
            dp[i] = i
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= num
    return dp[n%f]

print(cal(n,1000000))