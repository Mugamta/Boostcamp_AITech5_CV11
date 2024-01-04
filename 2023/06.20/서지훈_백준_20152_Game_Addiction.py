"""
상 하 좌 우 이동, 한 번 이동할때의 거리는 1, 최단경로 -> BFS (완전탐색)
경로의 개수를 구하라 -> 경로 탐색 문제가 아니게 변함 (경로 탐색을 N번하면 문제가 생김)


경로의 개수를 구하기 위해서는 특정 경로에서 어떤 경로까지 가는 방법의 수를 더하는 방법이 되어야 함
H와 N은 30 이내이므로, arr[H][N]은 메모리 제한에 걸리지 않음
따라서 동적 계획법으로  풀 수 있는 문제가 됨
"""

H, N = map(int, input().split())

if H == N:
    print(1)
else:
    A, B = max(H, N)+1, min(H, N)
    length = A - B
    path = [[0 for _ in range(A)] for _ in range(A)]

    for y in range(B, A):
        for x in range(B, A):
            if y <= x:
                path[y][x] = 1
    for y in range(B+1, A):
        for x in range(B+1, A):
            if y <= x:
                path[y][x] = path[y-1][x] + path[y][x-1]

    print(path[A-1][A-1])