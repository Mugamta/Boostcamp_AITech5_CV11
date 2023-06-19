# y > x인 곳은 침수 
H, N = map(int, input().split())

if H == N:
    print(1)
else:
    end = abs(H - N) + 1
    world = [[1] * end if i == 0 else [0] * end for i in range(end)]
    
    for i in range(1, end):
        for j in range(i, end):
            world[i][j] = world[i - 1][j] + world[i][j - 1]

    print(world[end-1][end-1])