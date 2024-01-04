from collections import deque

def main():
    
    n = int(input())
    m = int(input())
    
    routes = dict()
    
    for _ in range(m):
        start, end, cost = map(int, input().split(' '))
        if start not in routes:
            routes[start] = {end:cost}
        elif end not in routes[start]:
            routes[start][end] = cost
        else:
            if routes[start][end] > cost:
                routes[start][end] =cost

    shortest = [float('inf') for _ in range(n)]     ## 각 도시에 이르는 cost를 inf로 초기화
    
    start, end = map(int, input().split(' '))
    
    prev =[None for _ in range(n)]                  ## 각 도시에 이르는 최단거리 직전 도시를 저장
    shortest[start-1] = 0                           ## 시작 도시의 cost는 0으로
    
    queue = deque([start])                          ## deque에 start 도시 초기화
    while queue:
        o_city = queue.popleft()
        if o_city not in routes:                    
            continue
        for d_city, cost in zip(routes[o_city].keys(),routes[o_city].values()):
            if shortest[o_city-1]+cost < shortest[d_city-1]:        ## (직전 도시 최단 + 현재 cost)가 (기존 최단 거리(d) )보다 짧은 경우 update
                shortest[d_city-1] = shortest[o_city-1]+cost
                prev[d_city-1]= o_city                              ## 도시(d_city)에 최단 거리로 올 수 있는 직전 도시(o_city)
                queue.append(d_city)
        
    val = end
    arr= [end]
    while prev[val-1]:          ## end 지점 도시부터 최단 거리로 올 수 있는 직전 도시를 차례대로 추가 
        arr.append(prev[val-1])
        val = prev[val-1]
    
    print(shortest[end-1])
    print(len(arr))    
    print(' '.join([str(i) for i in arr[::-1]]))
    
    
main()