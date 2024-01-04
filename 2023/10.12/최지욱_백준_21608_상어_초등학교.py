def locate(student, prefer, board, N):      ## student를 위치시키는 함수
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    MAX_num = -1
    MAX_empty = -1
    cand_row, cand_col = 0 ,0
    
    for row in range(N):                    ## 행열을 순회
        for col in range(N):
            
            if board[row][col]:
                continue
            
            num = 0
            empty = 0
            
            for drow, dcol in dirs:         ## 각 4방향에 대해 탐색
                
                trow, tcol = row+drow, col+dcol
                if trow<0 or trow>=N or tcol<0 or tcol>=N:      ## 범위 이외 처리
                    continue
                
                if board[trow][tcol] in prefer:         ## 선호 학생이 있는 경우
                    num += 1
                elif board[trow][tcol] == False:        ## 빈 칸인 경우
                    empty += 1
                else:
                    pass
                
            if MAX_num < num:                           ## 이웃 선호 학생수가 갱신된 경우
                cand_row, cand_col = row, col           ## 후보 위치로 지정
                MAX_num = num                           ## 최대 이웃 선호 학생수 갱신
                MAX_empty = empty                       ## 빈 칸 개수 갱신

            elif MAX_num == num:                        ## 이웃 선호 학생수는 그대로이고
                if empty > MAX_empty:                   ## 빈 칸 개수가 갱신된 경우
                    cand_row, cand_col = row, col       ## 후보 위치로 지정
                    MAX_empty = empty                   ## 빈 칸 개수 갱신
                    
            else:
                pass
    
    board[cand_row][cand_col] = student                 ## 최적 위치로 student를 최종 설정하고 board를 반환
    return board
    

def get_score(board,prefer_dict, N):                ## 최종 선호 점수를 계산하는 함수
    score = 0              
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for row in range(N):                            ## 전체 행렬을 순회
        for col in range(N):
            
            num =0
            prefer_list = prefer_dict[board[row][col]]      ## 해당 위치의 학생이 선호하는 학생 리스트
            
            for drow, dcol in dirs:                 ## 각 4방향에 대해 탐색
                
                trow, tcol = row+drow, col+dcol
                if trow<0 or trow>=N or tcol<0 or tcol>=N:      ## 범위 이외 처리
                    continue
                
                if board[trow][tcol] in prefer_list:        ## 선호 학생인 경우 횟수 세어주기
                    num += 1
            
            ## 횟수에 따른 score 누적
            if num ==0:
                score += 0
            elif num==1:
                score += 1
            elif num==2:
                score += 10
            elif num==3:
                score += 100
            elif num==4:
                score += 1000
                
    return score        ## score 반환


def main():
    
    arr= []
    prefer_dict = {}
    
    N = int(input())
    
    for _ in range(N**2):
        row = list(map(int, input().split(' ')))
        arr.append(row)
        
    board = [[False for _ in range(N)] for i in range(N)]
    
    for row in arr:   
        
        student = row[0]    ## 학생
        prefer = row[1:]    ## 학생의 선호 리스트
        prefer_dict[student] = prefer       ## key:학생 / value:선호 학생 리스트
        
        board = locate(student, prefer, board, N)   ## 학생을 매번 위치시키도록
        
    print(get_score(board, prefer_dict, N))
    
main()