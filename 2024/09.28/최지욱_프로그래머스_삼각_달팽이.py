'''
시간 : 76.26ms
메모리 : 43.2MB
'''


def solution(n):
    arrs = [[-1] * (i + 1) for i in range(n)]
    t = n * (n + 1) // 2 
    
    down, right, up = n, n - 1, n - 2
    num, row, col = 0, -1, 0

    while num < t:
        
        # 아래
        for _ in range(down):
            row += 1
            num += 1
            arrs[row][col] = num
        
        down -= 3
        if num >= t: 
            break

        # 오른쪽
        for _ in range(right):
            col += 1
            num += 1
            arrs[row][col] = num

        right -= 3
        if num >= t: 
            break

        # 위
        for _ in range(up):
            row -= 1
            col -= 1
            num += 1
            arrs[row][col] = num

        up -= 3

    result = []
    for row in arrs:
        result += row 
        
    return result