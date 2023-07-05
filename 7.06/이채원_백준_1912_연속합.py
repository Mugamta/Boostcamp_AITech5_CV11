#입력 받기
import sys
n = map(int, sys.stdin.readline().split()) #n
arr = map(int, sys.stdin.readline().split()) #n개의 정수로 이루어진 List
answer = 0
temp = 0

for i, num in enumerate(arr) :
    if i == 0 : 
        temp = num
        answer = num
    else : 
        if temp+num < num : 
            temp = num
            answer = max(answer, temp)
            # print("case1")
            
        elif temp+num > temp : 
            temp += num
            answer = max(answer,temp)
            # print("case2")

        else : # temp+num < temp
            answer = max(answer, temp)            
            temp += num  
            # print("case3")

    # print(f'{num} : temp={temp}, answer={answer}')
print(answer)
