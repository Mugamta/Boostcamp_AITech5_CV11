#87에서 시간초과

import sys 

T = int(input()) # test case 개수

for i in range(T) :
    answer = 0
    N = int(input()) #날짜 수
    days = list(map(int, sys.stdin.readline().split()))

    # while len(days) :
    #     m = days.index(max(days))
    #     mx = days[m]
    #     if m != 0 :
    #         t = days[:m]
    #         answer += sum(list(mx-i for i in t))    
    #     days = days[m+1:]
        
    days.reverse()
    temp = 0
    for j in days :
        if j>temp :
            temp = j
        else :
            answer += temp - j

    print(f"answer : {answer}")
    # print(answer)