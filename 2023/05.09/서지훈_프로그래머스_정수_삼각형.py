def solution(triangle):
    answer = 0
    length = len(triangle)
    
    for i in range(1, length):
        triangle[i][0] += triangle[i-1][0]
        
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
        triangle[i][i] += triangle[i-1][i-1]
        
    print(max(triangle[length-1]))
    answer = max(triangle[length-1])

        
    return answer