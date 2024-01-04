def solution(tickets):
    tickets.sort()                  ## 티켓 정렬

    start = ["ICN"]                 ## 시작할 공항 ICN, 경로를 누적할 리스트
    used = [False] * len(tickets)   ## 사용한 ticket 여부를 판단

    return dfs(start, tickets, used)    ## dfs

def dfs(route, tickets, used):
    if False not in used:           ## 모두 ticket 사용했으면 route 반환
        return route

    for i in range(len(tickets)):   ## ticket을 순회하면서
        if not used[i] and route[-1] == tickets[i][0]:  ## 티켓을 사용하지 않았고 최종 경로가 ticket 시작 공항일 때
            used[i] = True          ## 티켓을 사용, (다음 공항으로 이동)
            next_route = dfs(route + [tickets[i][1]], tickets, used)    ## 다음 경로를 다시 탐색(기존 경로+다음공항, tickets, 사용후 티켓 리스트)

            if next_route:              ## 경로를 찾은 경우 return
                return next_route

            used[i] = False  # 경로가 유효하지 않으면 티켓 사용 취소 후 다음 티켓 탐색
