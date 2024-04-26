"""
ATM이 1대 밖에 없다.

i번째 사람이 돈을 인출하는데 걸리는 시간 P_i 
우리가 구해야하는 것

각 사람들이 인출하는데 걸리는 시간의 합의 최소

ex) 만약에 3명의 사람이 있고
P1 = 3, P2 = 4, P3 = 5
이고 1, 2, 3 순서라면

3 + (3 + 4) + (3 + 4 + 5) = 22가 걸린다.
"""
import sys

input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))

P.sort()
for i in range(1, N):
    P[i] = P[i-1] + P[i]

print(sum(P))