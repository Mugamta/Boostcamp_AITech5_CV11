"""
메모리 : 32140KB
시간 : 308ms
"""

def main():
    N = int(input())
    
    pair = {0:5,1:3,2:4,3:1,4:2,5:0}
    dices = []
    for _ in range(N):
        dices.append(list(map(int, input().split())))

    MAX = 0 
    for n in range(1,7):
        result = 0
        down = n 
        ## 맨 아래 주사위부터 최대값이 될 수 있는 옆면 구하기
        for i in range(len(dices)):
            ## [down, up]으로 제외되는 주사위 숫자 외에는 옆면이 가능
            down_index = dices[i].index(down)
            up = dices[i][pair[down_index]]
            if 6 not in [down, up]:
                result += 6
            elif 5 not in [down, up]:
                result += 5
            else:
                result += 4
            
            down = up

        ## 최대 옆면의 합 갱신
        MAX = max(MAX, result)
    print(MAX)   
    
if __name__=='__main__':
    main()