import math
import sys

n = int(input())

""" li[i]는 i번째 행성에서 i+1번째 행성으로 이동하기 위한 최소 속도를 의미한다. """
li = list(map(int, sys.stdin.readline().split()))

res = li[n-1]

""" 행성을 역순으로 순회 """
for i in range(n-2, -1, -1):
    
    """ 이전 속도가 더 크거나 같으면 문제없음 """
    if li[i] >= res:
        res = li[i]
    else:
        """ 이전 속도가 더 작으면 정수배가 필요함 """
        """ li[i] * x >= res -> x >= res / li[i] """
        """ 곱해져야하는 최소 값은 res / li[i] """
        """ 이는 정수가 아닐 수 있으므로 올림하고 정수로 바꿔줌 """
        res = li[i] * int(math.ceil(res / li[i]))
print(res)