'''
02:35
시작

02:50

이웃한 집(줄)간의 색이 같지 않아야 함
현재 줄이 r인경우 윗 줄의 (g,b)를 고려, g인 경우 (r,b), b인 경우 (r,g) 
각 줄마다 색을 선택할때 최소 비용을 구할 수 있음

'''


def main():
    
    N = int(input())
    
    min_r,min_g,min_b = map(int, input().split(" "))        ## 첫 줄을 입력, 첫 줄의 값은 최소 값
    
    for _ in range(N-1):
        
        r,g,b = map(int, input().split(" "))
        ## 윗 줄에서 최소값 두 개 중 작은 값과, 현재 줄의 값을 더하여 update
        prev_r, prev_g, prev_b = min(min_g, min_b), min(min_r, min_b),min(min_r, min_g)
        min_r = r+prev_r
        min_g = g+prev_g
        min_b = b+prev_b
    
    print(min(min_r, min_g, min_b))     ## 마지막 줄의 최소 값
    
main()