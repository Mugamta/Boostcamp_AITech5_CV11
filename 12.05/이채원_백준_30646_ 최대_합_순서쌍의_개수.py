import sys
from collections import defaultdict
# 3%에서 시간 초과
def solution():
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    ss_arr = []
    d = defaultdict(list)
    temp = 0
    for i in range(N) :
        d[arr[i]].append(i)
        temp += arr[i]
        ss_arr.append(temp)
    mx = 0  #최대 합
    num = 0 #순서쌍 개수


    for n in d.keys() :
        # for i in range(d[n][0], d[n][-1]+1) :
        #     temp += arr[i]
        temp = ss_arr[d[n][-1]] - ss_arr[d[n][0]] + arr[d[n][0]]
        
        if temp == mx :
            num += 1
        elif temp > mx : 
            mx = temp
            num = 1
    print(mx, num)
solution()