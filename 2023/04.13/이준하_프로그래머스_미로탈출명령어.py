# d -> l -> r -> u
# k가 최소거리보다 작은 경우 impossible
# 최소가 홀수면, k도 홀수, 짝수면, k도 짝수여야함 -> k-min_d가 짝수여야함
# 일단 최소 거리를 구한 뒤 impassible 검사하고,
# k 채울 수 있게 d 우선의 리스트 만들고, 정렬


def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    min_d = abs(x-r) + abs(y-c)
    key = k - min_d
    if key < 0:
        return answer
    elif key%2 == 1:
        return answer
    else:
        answer = ''
        ud = x-r
        lr = y-c
        if ud < 0 :
            for i in range(abs(ud)):
                answer += 'd'
        if lr > 0 :
            for i in range(abs(lr)):
                answer += 'l'
        if ud > 0 :
            for i in range(abs(ud)):
                answer += 'u'
        if lr < 0 :
            for i in range(abs(lr)):
                answer += 'r'
                
        dp = min( n-max(x,r), key//2)
        key -= dp*2

        lp = min( min(y,c)-1, key//2)
        key -= lp*2
        
        answer = 'd'*dp + answer
            
        a = answer.find('l')
        b = answer.find('r')
        c = answer.find('u')
        
        if a != -1:
            answer = answer[:a]+'l'*lp+answer[a:]
        elif b != -1:
            answer = answer[:b]+'l'*lp+answer[b:]
        elif c != -1:
            answer = answer[:c]+'l'*lp+answer[c:]
        else:
            answer = answer + 'l'*lp
        
        b = answer.find('r')
        c = answer.find('u')
        
        if b != -1:
            answer = answer[:b]+'rl'*(key//2)+answer[b:]
        elif c != -1:
            answer = answer[:c]+'rl'*(key//2)+answer[c:]
        else:
            answer = answer + 'rl'*(key//2)
        
        c = answer.find('u')
        
        if c != -1:
            answer = answer[:c]+'r'*lp+answer[c:]
        else:
            answer = answer + 'r'*lp
        
        answer += 'u'*dp

            
    return answer
