"""
  메모리 : 31120kb
  시간 : 44ms
"""
import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str, comb))))
        
nums.sort()
try:
    print(nums[n - 1])
except:    
    print(-1)
