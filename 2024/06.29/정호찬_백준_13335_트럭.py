"""
    메모리 : 31120 kb
    시  간 : 64 ms
"""
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
car = list(map(int, input().split()))
b = [0] * w
time = 0

while n or sum(b): # 종료조건 : 건널차가 없을때
    time += 1

    # 다리 한칸 이동
    b.pop(0)
    b.append(0)

    #하중을 넘지 않는다면 다리에 차 추가
    if n and (sum(b) + car[0]) <= l:
        b[-1] = car.pop(0)
        n -= 1

print(time)
