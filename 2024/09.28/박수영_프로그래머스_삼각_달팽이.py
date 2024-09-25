def solution(n):
    # 삼각형 및 최대값 설정
    triangle, n_limit = [], 0
    for i in range(1, n + 1):
        triangle.append([0] * i)
        n_limit += i
    
    # 필요 변수 정의
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    
    triangle[0][0] = 1 # 초기값
    r, c, d = 0, 0, 0
    num = 2
    
    # 채우기
    while num <= n_limit:
        # 1. 다음 위치 구하기
        nr = r + dr[d]
        nc = c + dc[d]
        
        # 2. 예외 처리
        try:
            if not triangle[nr][nc]: # 비었다 >> 업데이트
                r, c = nr, nc
                
            else: # 값이 있다 >> 방향만 전환
                d = (d + 1) % 3
                continue
        
        except IndexError: # 범위를 벗어났다 >> 방향만 전환
            d = (d + 1) % 3
            continue
            
        # 3. 숫자 채우기
        triangle[r][c] = num
        num += 1
            
    # 4. 순서대로 합치기
    answer = []
    for row in triangle:
        answer.extend(row)
        
    return answer
