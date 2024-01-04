def main():
    n =int(input())
    a, b = map(int, input().split())
    
    m = int(input())
    arr = [None for _ in range(n+1)]        ## parent arr (child -> parent)
    
    for _ in range(m):
        parent, child = map(int, input().split())
        arr[child]= parent                  ## child에 대한 parent를 저장
        
    a_parents = set()
    a_list = []
    while a:                        ## a의 조상 찾아서 모두 추가
        a_parents.add(a)
        a_list.append(a)
        a = arr[a]                  ## 다음 parent 탐색

    num =0
    while b:
        if b in a_parents:          ## b가 a의 조상 중에 포함될 때
            print(num+a_list.index(b))  ## 현 지점까지의 거리(촌수) 
            return 0
        
        b = arr[b]                  ## 다음 parent 탐색
        num += 1

    print(-1)                       ## 못 찾을 경우 -1을 return

main()