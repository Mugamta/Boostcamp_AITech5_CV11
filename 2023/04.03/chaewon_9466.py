#백준 n9466 텀 프로젝트

#12:00 문제 읽기 시작 -> 해시? -> DFS
#12:42 첫 제출 -> 틀렸습니다
#1:24 수정 후 두번째 제출 -> 76%에서 시간초과

import sys
from collections import deque

def project(N,arr) : #프로젝트 팀에 속하지 못한 학생들 수 나타내기
    answer = 0 #팀에 속하지 못한 학생 수 
    
    arr = deque((i,arr[i]) for i in range(N))
    one = deque()   
    T = list(True for i in range(N))
    for i in range(N) :
        if T[i] :
            one.append(arr[i])
            team = []
            while one :
                s, w = one.pop()
                s += 1 
                team.append(s)

                # print("s,w : ",s,w)
                # print("answer  : ", answer)
                if s == w : #자기 자신을 가리키고 있을때 
                    for t in team :
                        T[t-1] = False 
                    answer += (len(team) - 1)
                    
                    # print("스스로 가리킴", team)
                    # print("answer : ", answer)


                else :
                    if T[w-1] : #가리킬 수 있는 학생

                        if w in team : #circle 완성
                            idx = team.index(w)
                            answer += idx
                            for t in team :
                                T[t-1] = False 
                            # print("team : ", team)
                            # print("answer : ", answer)
                            

                        else : 
                            one.append(arr[w-1]) 

                    else : #가리킬 수 없는 학생
                        T[s-1] = False 
                        for t in team :
                            T[t-1] = False
                        answer += len(team)
                        # print("가리킬 수 x ", answer)



           
    return answer


T = int(input())
for test_case in range(T) :
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    print(project(N, arr)) 


    