import sys


def func():
    N, M = map(int, sys.stdin.readline().split())
    
    s = set()
    for _ in range(N):
        s.add(sys.stdin.readline().rstrip())
    
    for _ in range(M):
        li = list(sys.stdin.readline().rstrip().split(','))
        for word in li:
            if word in s:
                s.remove(word)
                N -= 1
        sys.stdout.write(str(N) + "\n")
        

func()
