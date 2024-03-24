from heapq import heappop, heappush
import sys

def main():
    n = int(input())
    arr = []

    for _ in range(n):
        s, e = map(int, sys.stdin.readline().split())
        arr.append([s, e-1])

    arr.sort()  # 강의 시작 시간 기준으로 정렬
    cnt = 0
    heap = []   # 각 강의실의 종료 스케줄 저장

    for s, e in arr:
        # 기존 강의실에 이어서 강의가 가능한 경우(해당 강의가 최소 강의 종료 시점보다 후행하는 경우)
        if heap and heap[0] < s:
            heappop(heap)
        # 기존 강의실에 이어서 강의가 불가능한 경우(해당 강의가 최소 강의 종료 시점보다 선행하는 경우)
        else:
            cnt += 1
        heappush(heap, e)  # 강의의 끝나는 시간 추가

    print(cnt)
    return 0

if __name__ == '__main__':
    main()
