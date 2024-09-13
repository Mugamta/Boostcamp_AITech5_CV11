"""
시 간 :
메모리 : 

문제 풀이 : 
    상범 빌딩에 갇혀있음
    상범 빌딩은 각 변의 길이가 1인 정육면체 (단위 정육면체)로 이루어져 있음

    각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나
    비어 있어서 지나갈 수 있다.

    인접한 칸 (동, 서, 남, 북, 상, 하) 로 1분의 시간을 들여서 이동할 수 있다.
    대각선 이동은 불가

    구해야하는 것은 탈출하는데 걸리는 시간

입력 : 
    L (상범 빌등 층수), R, C (상범 빌딩의 한 층의 행과 열)

"""
import sys
from collections import deque

input = sys.stdin.readline
moves = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def main():
    L, R, C = map(int, input().split())
    if not (L+R+C):
        return 0
    
    buildings = []
    vis = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    for l in range(L):
        floor = []
        for r in range(R):
            rooms = list(map(str, input().strip()))
            for c in range(C):
                if rooms[c] == 'S':
                    start = (l, r, c) # 시작 위치
                    vis[l][r][c] = 1
                    break
            floor.append(rooms)
        input()
        buildings.append(floor)

    q = deque([start])

    while q:
        l, r, c = q.popleft()

        for dl, dr, dc in moves:
            nl, nr, nc = l+dl, r+dr, c+dc

            #방문 했는지, 방문 가능한지 체크
            if not (0<=nl<L and 0<=nr<R and 0<=nc<C):
                continue

            if buildings[nl][nr][nc]=='E':
                print(f"Escaped in {vis[l][r][c]} minute(s).")
                main()
                return 0
            
            if  buildings[nl][nr][nc] == '.' and not vis[nl][nr][nc]:
                vis[nl][nr][nc] = vis[l][r][c] + 1
                q.append((nl, nr, nc))
                
    print("Trapped!")
    main()
    return 0

if __name__ =="__main__":
    main()
    

