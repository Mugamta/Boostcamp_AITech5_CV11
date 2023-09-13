def verify(line):
    for i in range(line):
        if visited[line] == visited[i] or line - i == abs(visited[line] - visited[i]):
            return 0
    return 1


def n_queens(line):
    global result
    if line == N:
        result += 1
        return
    for i in range(N):
        visited[line] = i
        if verify(line) == 1:
            n_queens(line + 1)


def func():
    n_queens(0)
    print(result)


result = 0
N = int(input())
visited = [1] * N
func()
