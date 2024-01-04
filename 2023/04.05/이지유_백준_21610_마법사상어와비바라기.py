# 19:14 [START]
# 19:46 Simulation: Brute-forcing + Clockwise
# 20:07 {WA, 85} fix clouds initialization coordinates
# 20:13 {WA, 61} fix clouds initialization coordinates
# 20:19 {WA, 64} fix step 4 (misunderstood directions)
# 20:31 {WA, 82} fix step 3 coordinates
# 20:35 [AC]

import sys

input = sys.stdin.readline
dx1, dy1 = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx2, dy2 = [-1, -1, 1, 1], [-1, 1, 1, -1]

# Input.
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# Compute.

# Initialize list of clouds.
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for _ in range(M):
    D, S = map(int, input().split())
    
    visited = [[False] * N for _ in range(N)]
    
    # Step 1, 2, 3-1.
    for i in range(len(clouds)):
        x, y = clouds[i]

        nx = (x + dx1[D] * S) % N
        ny = (y + dy1[D] * S) % N
        
        visited[nx][ny] = True
        clouds[i] = (nx, ny)

        A[nx][ny] += 1
    
    # Step 4.
    for x, y in clouds:
        cnt = 0

        for d in range(4):
            nx = dx2[d] + x
            ny = dy2[d] + y

            if (0 <= nx and N > nx and 0 <= ny and N > ny and A[nx][ny]):
                cnt += 1

        A[x][y] += cnt

    # Step 3-2.
    clouds = []

    # Step 5.
    for x in range(N):
        for y in range(N):
            if 2 <= A[x][y] and not visited[x][y]:
                A[x][y] -= 2
                clouds.append((x, y))
                
# Output.
print(sum(sum(i) for i in A))