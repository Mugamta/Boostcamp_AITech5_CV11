def solution(m, n, startX, startY, balls):
    answer = []
    for i in range(len(balls)) :
        endX, endY = balls[i][0], balls[i][1]
        temp = []
        #Case 1 : x 좌표가 동일할 때
        if startX == endX :
            temp.append(4*startX*endX+(startY-endY)*(startY-endY))
            temp.append(4*(m-startX)*(m-endX)+(startY-endY)*(startY-endY))
            if startY<endY : temp.append((startY+endY)*(startY+endY))
            else : temp.append((2*n-startY-endY)*(2*n-startY-endY))
            answer.append(min(temp))
        #Case 2 : y 좌표가 동일할 때
        elif startY == endY :
            temp.append(4*startY*endY+(startX-endX)*(startX-endX))
            temp.append(4*(n-startY)*(n-endY)+(startX-endX)*(startX-endX))
            if startX<endX : temp.append((startX+endX)*(startX+endX))
            else : temp.append((2*m-startX-endX)*(2*m-startX-endX))
            answer.append(min(temp))
        #Case 3 : x, y 좌표 모두 다를 때 
        elif startX != endX and startY != endY:
            temp.append((endX-startX)*(endX-startX)+(endY+startY)*(endY+startY))
            temp.append((endX+startX)*(endX+startX)+(endY-startY)*(endY-startY))
            temp.append((endY-startY)*(endY-startY)+(2*m-startX-endX)*(2*m-startX-endX))
            temp.append((endX-startX)*(endX-startX)+(2*n-startY-endY)*(2*n-startY-endY))
            answer.append(min(temp))
    return answer
