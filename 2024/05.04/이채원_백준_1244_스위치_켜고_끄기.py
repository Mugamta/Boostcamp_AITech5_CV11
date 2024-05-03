#메모리 31120 KB
#시간 40 ms

import sys

N = int(sys.stdin.readline()) #스위치의 개수
switch = list(map(int, sys.stdin.readline().split())) # 각 스위치의 상태 
M = int(sys.stdin.readline()) #학생 수 
student = list(list(map(int,sys.stdin.readline().split())) for _ in range(M)) #각 학생의 성별과 받은 수

for i in range(len(student)) : #각 학생마다
    
    s, n = student[i] 

    if s == 1 : #남학생일 경우
        for j in range(1, N+1) :
            if j%n == 0 : #배수가 되는 번호의 스위치 상태 변경
                
                if not switch[j-1] : switch[j-1] = 1
                else : switch[j-1] = 0
                

    elif s == 2 : #여학생일 경우 
        if switch[n-1] : switch[n-1]=0
        else : switch[n-1] = 1
        temp = 0 
        while True : 
            temp += 1
            t_m = n-temp 
            t_p = n+temp
            if t_m>0 and t_p<N+1 : 
                if switch[t_m-1]==switch[t_p-1] : # 대칭이면
                    if switch[t_m-1] : 
                        switch[t_m-1] = 0 
                        switch[t_p-1] = 0
                    else : 
                        switch[t_m-1] = 1 
                        switch[t_p-1] = 1
                else : break
            else : break
line = N//20 + 1
for i in range(line) : 
    if i == line - 1 :
        sw = switch[0 + 20*i :]
    else :
        sw = switch[0+ 20*i : 20 + 20*i]
    
    print(' '.join(list(str(i) for i in sw)))


