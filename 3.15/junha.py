import sys
from collections import defaultdict

input = sys.stdin.readline

dict = defaultdict(int)

N = int(input())

for _ in range(N):
    A = input()
    dict[A] += 1

sorted_dic = sorted(dict.items(), key = lambda x : (-x[1],x[0]))

print(sorted_dic[0][0])