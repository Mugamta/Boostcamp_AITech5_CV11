#관찰 : +면 그냥 넘어가고 - 면 괄호를 열어준다. 다시 -가 나올때 닫아준다. 

s = input()
d = []  #데큐 썼을때 136ms, 리스트 썼을때 116ms
answer = 0
temp = False
tempnum = 0

for t in s :
    if t.isdigit() : # 숫자면 deque에 
        d.append(t)

    if t == '+' : 
        tempnum += int(''.join(d))
        d = [] #d 초기화

    elif t =='-' : 
        if temp==False : #괄호 시작 전이라면
            if d : 
                tempnum += int(''.join(d))
                d = [] #d 초기화
            answer += tempnum 
            tempnum = 0
            temp = True #괄호 시작

        else : #괄호 시작 후라면
            tempnum += int(''.join(d))
            d = [] #d 초기화
            answer -= tempnum
            tempnum = 0

tempnum += int(''.join(d))

if temp == True :  answer -= tempnum
else : answer += tempnum

print(answer)       

        

