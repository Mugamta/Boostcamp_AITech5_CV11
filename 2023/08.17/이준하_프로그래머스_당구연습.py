def solution(m, n, startX, startY, balls):
    answer = []
    start = [startX,startY]
    for i,j in balls:
        end = [i,j]
        distance = 10**10
        temp = []
        if start[0]!=end[0] or start[1] > end[1]:  #두 점의 행이 같으면서, 시작점이 끝점보다 왼쪽인 경우
            temp.append(abs(start[0]-end[0])**2 + abs(2*n-start[1]-end[1])**2)  #우 벽의 크기 - 각 값
        if start[0]!=end[0] or start[1] < end[1]: 
            temp.append(abs(start[0]-end[0])**2 + abs(start[1]+end[1])**2)      #좌
        if start[1]!=end[1] or start[0] < end[0]: 
            temp.append(abs(start[0]+end[0])**2 + abs(start[1]-end[1])**2)      #상
        if start[1]!=end[1] or start[0] > end[0]: 
            temp.append(abs(2*m-start[0]-end[0])**2 + abs(start[1]-end[1])**2)  #하
        for dist in temp:
            if dist < distance:
                distance = dist
        answer.append(distance)
    return answer