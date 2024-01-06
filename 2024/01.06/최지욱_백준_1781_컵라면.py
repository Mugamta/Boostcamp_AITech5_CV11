import heapq

def main():
    
    n = int(input())
    dic = {i+1:[] for i in range(n)}
    
    for _ in range(n):
        dl, cup = map(int, input().split(' '))
        dic[dl].append(cup)                 ## 데드라인별로 받을 수 있는 컵라면들
    
    heap = []
    total = 0
    for i in range(n,0,-1):                 ## 데드라인이 긴 컵라면 수부터 차례로 탐색
        for num in dic[i]:
            heapq.heappush(heap,-num)       ## 큰 것부터 pop하기 위해 음수로 push
        if heap:
            MAX = -heapq.heappop(heap)      ## 해당 데드라인에서 가장 많이 받을 수 있는 컵라면 수 Pop(음수 값은 양수로 복구)
            total += MAX                     ## 컵라면 수는 누적
    
    print(total)
    return 0


if __name__ == '__main__':
    main()
