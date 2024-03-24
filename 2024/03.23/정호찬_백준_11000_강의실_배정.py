import heapq
import sys

input = sys.stdin.readline

n = int(input())

lecture_list = [list(map(int, input().split())) for _ in range(n)]
lecture_list.sort()

lecture_queue = []
heapq.heappush(lecture_queue, lecture_list[0][1])

for i in range(1, n):
    if lecture_list[i][0] < lecture_queue[0]:
        heapq.heappush(lecture_queue, lecture_list[i][1])
    else:
        heapq.heappop(lecture_queue)
        heapq.heappush(lecture_queue, lecture_list[i][1])

print(len(lecture_queue))