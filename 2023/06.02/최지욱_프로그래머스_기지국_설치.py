def solution(n, stations, w):
    stations = [-w] +stations +[n+w+1]      ## w만큼 더 뺀 지점, 더한 지점에 station이 있다고 가정
    empty = []                              ## 빈 공간마다 필요한 기지국의 개수를 넣을 리스트
    for i in range(len(stations)-1):
        dist = max(stations[i+1]-stations[i]- 2*w -1,0)     ## dist = (station간 거리 - 양쪽 도달 가능거리 - 1) or 0
        empty.append((dist-1)//(2*w+1)+1)   ## 필요한 기지국 갯수 = 거리 // 기지국 coverage                
    return sum(empty)