import math

def solution(n, stations, w):
    answer = 0

    radio = 2 * w + 1
    answer += math.ceil((stations[0] - w - 1) / radio)

    length = len(stations)
    for i in range(length-1):
        answer += math.ceil((stations[i+1] - stations[i] - 2 * w - 1) / radio)
    answer += math.ceil((n - stations[length-1] - w) / radio)

    return answer