'''
메모리 : 42656KB
시간 : 124ms
'''
import sys
import heapq

def main():
    
    N = int(input())
    arr = [int(sys.stdin.readline()) for _ in range(N)]
    heap = []
    
    for i in arr:
        ## pop operation
        if i ==0:
            if len(heap):
                _, target = heapq.heappop(heap)
                print(target)
            else:
                print(0)
                
        ## push operation
        else:
            heapq.heappush(heap, [abs(i),i])

    return 0

if __name__ =='__main__':
    main()