#백트래킹 연습

def back(n) : 
    global answer 
    if n == N : #퀸을 N개 모두 다 놓았다면
        answer += 1 
    else : 
        for i in range(N) : #모든 자식 노드에 대해
            if visited[i] == False : #퀸이 놓이지 않은 열이라면
                board[n] = i #퀸을 놓는다
                if check(n) : #유망하다면 (퀸을 놓는게 가능하다면)
                    visited[i] = True #자식노드로 이동
                    back(n+1)         #백트래킹
                    visited[i] = False # 다시 부모노드로 이동

def check(m) : #m은 특정 depth, 해당 위치에 퀸이 놓이는 것이 가능한지 여부를 확인
    for i in range(m) :
        if board[m] == board[i] or m-i == abs(board[m]-board[i]) : #같은 열에 있거나, 대각선에 있거나
              return False
    return True 


#main 
if __name__ == '__main__' :
    N = int(input()) 

    board = [0 for _ in range(N)]
    visited = [False for _ in range(N)]
    answer = 0

    back(0)
    print(answer)