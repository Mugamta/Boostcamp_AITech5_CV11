def solution(m, n, startX, startY, balls):
    arr = []
    for ball in balls:
        X, Y = ball 
        targets = [[X,-Y],[-X,Y],[2*m-X,Y],[X,2*n-Y]]
        distances = [(x-startX)**2 + (y-startY)**2 for (x, y) in targets if ((x-startX)**2 + (y-startY)**2 < (X-x)**2 + (Y-y)**2) or (x!=startX and y!= startY)]
        arr.append(min(distances))

    return arr