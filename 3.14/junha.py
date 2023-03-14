import sys
input = sys.stdin.readline
num = int(input())
arr = [list(map(int, input().split())) for _ in range(num)]

answer = 0

def check(arr,p1,p2,p3):
    a1 = ((arr[p2][0] - arr[p1][0]) * (arr[p3][0] - arr[p1][0]) + (arr[p2][1] - arr[p1][1]) * (arr[p3][1] - arr[p1][1])) 
    a2 = ((arr[p1][0] - arr[p2][0]) * (arr[p3][0] - arr[p2][0]) + (arr[p1][1] - arr[p2][1]) * (arr[p3][1] - arr[p2][1])) 
    a3 = ((arr[p1][0] - arr[p3][0]) * (arr[p2][0] - arr[p3][0]) + (arr[p1][1] - arr[p3][1]) * (arr[p2][1] - arr[p3][1]))
    return a1*a2*a3
            
for p1 in range(num - 2):
    for p2 in range(p1 + 1, num - 1):
        for p3 in range(p2 + 1, num):
            if check(arr,p1,p2,p3) == 0:
                answer += 1
print(answer)
