'''
메모리 : 31120KB
시간 : 44ms
'''

def main():
    
    N = int(input())
    arr = list(map(int, input().split()))
    
    for _ in range(int(input())):
        gender, target = map(int, input().split())
        
        ## 남학생인 경우 배수의 스위치 바꾸기
        if gender==1:
            for i in range(target, N+1, target):
                arr[i-1] = (arr[i-1]+1)%2
        
        ## 여학생인 경우 최대 대칭 지점(left, right)까지 스위치 바꾸기
        elif gender==2:
            left = target-2
            right = target
            arr[target-1] = (arr[target-1]+1)%2
            
            while (left>=0) and (right<N):
                if arr[right]==arr[left]:
                    arr[right] = (arr[right]+1)%2
                    arr[left] = (arr[left]+1)%2
                    left -= 1
                    right += 1
                else:
                    break
    ## 20개 단위로 출력
    for n in range(0, N+1, 20):
        print(" ".join([str(i) for i in arr[n:n+20]]))
    return 0


if __name__ == '__main__':
    main()