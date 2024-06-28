import sys
input = sys.stdin.readline

n,w,l= map(int, input().split()) #트럭 수, 다리 길이, 최대 하중
trucks = list(map(int, input().split()))
time = 0
stack = [0]*w #현재 다리 위 상태



while trucks:
    time += 1
    stack.pop(0)
    if sum(stack) + trucks[0] <= l:
        stack.append(trucks.pop(0))
    else :
        stack.append(0)
print(time+ len(stack))
