'''
메모리 : 31120KB
시간 : 84ms
'''

import sys

def rotate(string, dir):
    
    ## counter clockwise
    if dir==-1:
        string = string[1:]+string[0]
    ## clockwise
    elif dir==1:
        string = string[-1]+string[:-1]
    return string

def main():
    
    N = int(input())
    arr = [input() for _ in range(N)]

    for _ in range(int(input())):
        
        num, dir = map(int, sys.stdin.readline().split())
        
        prev_left = arr[num-1][6]
        prev_right = arr[num-1][2]
        right_dir, left_dir = dir, dir
        arr[num-1]= rotate(arr[num-1], dir)
        
        ## 왼쪽방향 톱니 회전
        for i in range(num-2, -1, -1):        
            if arr[i][2]== prev_left:
                break
            else:
                right_dir *= -1
                prev_left = arr[i][6]
                arr[i] = rotate(arr[i], right_dir)
        
        ## 오른쪽방향 톱니 회전
        for i in range(num, N, 1):
            if arr[i][6]== prev_right:
                break
            else:
                left_dir *= -1
                prev_right = arr[i][2]
                arr[i] = rotate(arr[i], left_dir)

    print(sum([int(i[0]) for i in arr]))
    return 0


if __name__ == '__main__':
    main()