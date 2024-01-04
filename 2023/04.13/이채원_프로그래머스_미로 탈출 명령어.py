
def solution(n, m, x, y, r, c, k):
    answer = ''
    distance = abs(x-r) + abs(y-c)
    
    #case 제외 : k번 안에 갈 수 없는 경우
    if distance > k  or abs(distance-k) % 2 != 0 : return "impossible"    

    d = (k - distance)//2 # 잉여 거리
    
    dd,ll,rr,uu = 0,0,0,0

    if x<r :  dd = r-x #down
    else: uu = x-r #up
    if c<y : ll = y-c #left
    else : rr = c-y #right

    d_rem = min( n-max(x,r), d)
    d -= d_rem

    l_rem = min( min(y,c)-1, d)
    d -= l_rem

    answer = 'd'*(dd+d_rem)+'l'*(ll+l_rem)+'rl'*(d)+'r'*(rr+l_rem)+'u'*(d_rem+uu)
    




    return answer