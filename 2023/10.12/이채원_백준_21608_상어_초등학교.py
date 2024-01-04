import sys

N =  int(input())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N*N))
cls = list(list( 0 for _ in range(N)) for _ in range(N)) #좌석배치표
ij = [[-1,0], [0,-1], [1,0], [0,1]] #인접 칸 (상하좌우)

#자리 배치하기

for i in range(N*N) :
    stu, a, b, c, d = arr[i] 
    like = 0
    empty = 0
    temp_row = N+1
    temp_col = N+1
    for row in range(N) :
        for col in range(N) : 
            if cls[row][col] == 0 : #빈칸일 경우만
                temp_empty = 0
                temp_like = 0

                for m in range(4) : #인접한 4 칸 검사
                    new_row = row + ij[m][0] 
                    new_col = col + ij[m][1]

                    if (0 <= new_row < N) and (0 <= new_col < N) : #보드 범위 안일 경우
                            if cls[new_row][new_col] == 0 : #빈칸일 경우
                                temp_empty += 1
                            elif cls[new_row][new_col]==a or cls[new_row][new_col]==b or cls[new_row][new_col]==c or cls[new_row][new_col]==d: #좋아하는 친구가 있을 경우
                                temp_like += 1
                
                if temp_like > like : #인접한 칸에 좋아하는 친구가 더 많을 경우
                    temp_row = row
                    temp_col = col
                    like = temp_like
                    empty = temp_empty

                elif temp_like == like : #인접한 칸에 좋아하는 친구 수가 같을 경우 빈칸 수 비교
                    if temp_empty > empty : # 빈칸이 더 많을 경우
                        temp_row = row
                        temp_col = col
                        like = temp_like
                        empty = temp_empty

                    elif temp_empty == empty : #빈칸 수 같을 경우 행열 비교
                        if row<temp_row : #행이 더 작을 경우 
                            temp_row = row
                            temp_col = col
                            like = temp_like
                            empty = temp_empty
                        elif row == temp_row : #행이 같을 경우 열 비교
                            if col < temp_col : 
                                temp_row = row
                                temp_col = col
                                like = temp_like
                                empty = temp_empty
            # print(f"i:{i}, row, col : [{row}, {col}], temp_r,c :[{temp_row}, {temp_col}] empty:{empty}, like:{like}")    

    cls[temp_row][temp_col] = stu                                      
# print(f"자리배치 : {cls}")

#만족도 구하기

arr.sort(key= lambda x : x[0])
score = [0,1,10,100,1000]
answer = 0
for row in range(N) :
    for col in range(N) :         
        stu = cls[row][col]
        a, b, c, d = arr[stu-1][1],arr[stu-1][2],arr[stu-1][3],arr[stu-1][4]
        temp_like = 0
        for m in range(4) : #인접한 4 칸 검사
            new_row = row + ij[m][0] 
            new_col = col + ij[m][1]

            if (0 <= new_row < N) and (0 <= new_col < N) : #보드 범위 안일 경우
                    if  cls[new_row][new_col]==a or cls[new_row][new_col]==b or cls[new_row][new_col]==c or cls[new_row][new_col]==d: #좋아하는 친구가 있을 경우
                        temp_like += 1
        
        answer += score[temp_like]

# print(f"score : {answer}")
print(answer)