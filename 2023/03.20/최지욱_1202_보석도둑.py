'''
15:45

비싼 보석 순으로 탐색
heapq / list
비싼 보석을 담을수 있는 가방은 가장 작은 가방 순으로 탐색

보석 값이 비싼 순서대로 heapq 이용
가방 크기가 작은 순서대로 list 정렬하여 이용
-> 비싼 보석 순으로 최대한 작은 가방에 넣기

16:19 
10%에서 시간초과 

16:50
------------------------------

최소 가방을 기준 최대 보석을 찾기

->최소 가방에 들어갈 수 있는 모든 보석을 price를 기준으로 push
->매번 가방마다 최대 price 보석을 pop

가장 작은 가방 크기부터 순서대로, 들어갈수 있는 모든 보석을 heapq에 가격을 기준으로 max heap에 push
해당하는 가방에서 들어갈 수 있는 최선의 보석(최대 가격)을 구하기

'''

import heapq
import sys

def main():
    
    gem_list = []
    max_weight =[]
    total_price =0
    
    gem_num, bag_num = list(map(int, sys.stdin.readline().split()))
    
    for _ in range(gem_num):
        weight, price = list(map(int, sys.stdin.readline().split()))
        heapq.heappush(gem_list,[weight, price])        ## 낮은 무게를 갖는 보석순으로 min heapq 생성

    for _ in range(bag_num):
        max_weight.append(int(sys.stdin.readline().rstrip()))
            
    max_weight.sort()   ## weight 작은 순서대로 가방 sort
    max_price_list =[]
    
    for index, weight in enumerate(max_weight):
        while gem_list:
            if weight>=gem_list[0][0]:          ## 가방에 담을 수 있는 보석 무게인 경우
                heapq.heappush(max_price_list, -(heapq.heappop(gem_list)[1]))    ## price가 높은 순으로 max heapq 생성
            else:
                break
        
        if max_price_list:
            total_price -= heapq.heappop(max_price_list)
        elif not gem_list:
            break

    print(total_price)

main()