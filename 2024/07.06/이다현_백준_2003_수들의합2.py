n,m = map(int, input().split()) #수열 길이, 수열의 합
lst = list(map(int, input().split()))

st, end = 0,0
ans = 0
total = lst[0]

while 1:
    if total < m:
        end += 1
        if end >= n:
            break
        total += lst[end]
    elif total > m :
        total -= lst[st]
        st += 1
    if total == m:
        ans+=1
        end += 1
        if end >= n:
            break
        total += lst[end]

print(ans)
