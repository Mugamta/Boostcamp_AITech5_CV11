N = int(input())
S = list(input())

def check(str,piv):
    cnt = 0
    max = 0
    for word in str:
        if piv == word:
            cnt += 1
            if max < cnt:
                max = cnt
        else:
            cnt -= 1
    return max


if S.count('(') != S.count(')'):
    print(-1)
else:
    answer = max(check(S,'('),check(S,')'))
    print(answer)