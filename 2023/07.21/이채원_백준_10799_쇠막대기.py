import sys
from collections import deque

lst =sys.stdin.readline().split()
lst = list(lst[0])

answer = 0

d = deque()

m = 0 #막대
temp = False
now = False

for i in range(len(lst)) :
    if len(d)== 0 :
        
        d.append(lst[i])
        m = 1
        temp = True

        print(f"case0-{lst[i]}:{answer}")
    elif lst[i] == '(' :
        if not temp : 
            answer += m-1
        d.append(lst)
        m += 1
        temp = True

        print(f"case1-{lst[i]}:{answer}")
    elif lst[i] == ')' :
        d.pop()
        if temp : 
            m-=1
            answer += m 
            temp = False
            print(f"case2-0-{lst[i]}:{answer}") 
        else :
            m -= 1
            print(f"case2-1-{lst[i]}:{answer}")
print(answer)



    