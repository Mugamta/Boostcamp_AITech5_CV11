def solution(routes):
    routes.sort(key=lambda x : x[1])
    present = -30001
    cnt = 0
    for i in routes:
        if i[0] > present:
            cnt += 1
            present = i[1]
    return cnt
