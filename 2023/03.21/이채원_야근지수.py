#프로그래머스 야근 지수 LV.3//3월21일 

#10:20 시작 : 무조건 가장 큰 숫자를 -1 하는게 피로도를 최소화하는 방법인것같음
#"최댓값"을 뽑아내 -1을 한 다음 그걸 다시 리스트에 넣고 "또 정렬"해야 함
# ==> 계속계속 순서가 중요하네 ==> 최대힙을 써야겠다!
#10:33 통과


def solution(n, works):
    import heapq as hp 
    answer = 0
    if sum(works) <= n : return 0
    h = list(-x for x in works) #최대 힙 구현
    hp.heapify(h)
    for i in range(n) : 
        temp =  hp.heappop(h) +1 #최댓값 뽑아 1 줄임
        if temp : hp.heappush(h, temp) #0이 아니라면 push
    return(sum(list(x*x for x in h)))

