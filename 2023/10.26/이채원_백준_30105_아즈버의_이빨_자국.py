import sys

N = int(input()) #이빨 자국 개수
arr = list(map(int, sys.stdin.readline().split()))


if N == 2 :
    print("1")
    print(str(arr[1]-arr[0]))

else :

    answer = []
    lst = []

    for i in range(1, N//2+1) : #송곳니의 간격 후보
        lst.append(arr[i]-arr[0])

    # print(f"lst={lst}")


    for i in lst :
        check = list(False for _ in range(N)) #전부다 확인됐는지 
        for j in range(N-1) :
            if check[arr.index(arr[j])]==False :
                t = arr[j] + i

                if t not in arr : 
                    break

                else :
                    check[arr.index(arr[j])] = True
                    check[arr.index(t)] = True 
                
        z = 0
        for j in range(N) :
            if check[j] == False : 
                if arr[j] + i in arr or arr[j] -i in arr :
                    pass
                else :
                    z += 1
        
        if z == 0 : 
            answer.append(str(i))


    print(str(len(answer)))
    print(' '.join(answer))


