import sys
input=sys.stdin.readline

N=int(input())
map=[input().strip() for i in range(N)]

def quad(x, y, n) :
    # 1. 주어진 영상이 분할 정복의 최소 단위(1 x 1)인 경우
    if n == 1 :
        return map[x][y]

    # 2. 주어진 영상이 분할 정복의 최소 단위(1 x 1)가 아닌 경우    
    area1 = quad(x, y, n // 2)  
    area2 = quad(x + n // 2, y, n // 2)  
    area3 = quad(x, y + n // 2, n // 2)
    area4 = quad(x + n // 2, y + n // 2, n // 2)
    
    # 2.1. 주어진 영상이 모두 같은 비트인 경우
    if area1 == area2 == area3 == area4 and len(area1) == 1 :
        return area1
 
    # 2.2. 주어진 영상이 모두 같은 비트가 아닌 경우
    return "(" + area1 + area2 + area3 + area4 + ")"

print(quad(0, 0, N))