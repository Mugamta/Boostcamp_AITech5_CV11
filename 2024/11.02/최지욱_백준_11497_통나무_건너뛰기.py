"""
메모리 : 32140KB
시간 : 204ms
"""

def main():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        arr = list(map(int,input().split()))
        arr.sort()
        
        arr1 = [arr.pop()]
        arr2 = []

        ## 최소 난이도 통나무 배열 생성
        ## 가장 높은 통나무에서 각각 양쪽 방향으로
        ## 차이가 적은 배열을 만들고, 두 배열 결합
        while arr:
            arr1.append(arr.pop())
            if arr:
                arr2.append(arr.pop())
                
        steps = arr1+arr2[::-1]
        
        
        ## 초기 난이도(첫 통나무, 마지막 통나무)
        level = abs(steps[0]-steps[-1])
        
        ## 원 형태의 배열에서 난이도 구하기
        for i in range(len(steps)-1):
            level = max(level, abs(steps[i]-steps[i+1]))
        
        print(level)


if __name__=='__main__':
    main()