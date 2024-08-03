from collections import Counter
def solution(topping):
    answer = 0
    dic = Counter(topping)
    bro = {}
    for i in range(len(topping)):
        tmp = topping[i]
        if tmp in bro:
            dic[tmp] -= 1
            bro[tmp] += 1
        else :
            dic[tmp] -= 1
            bro[tmp] = 1
        if dic[tmp] == 0:
            del dic[tmp]
        if len(dic) == len(bro):
            answer += 1
    return answer
