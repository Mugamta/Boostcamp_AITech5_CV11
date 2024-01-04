# 모든 값의 최대공약수를 구하는 문제
from math import gcd
li=[]
n,s=list(map(int,input().split()))
A=list(map(int,input().split()))
for i in A:
    li.append(abs(s-i)) #수빈이와 동생들의 거리 차이
D=li[0]
for i in range(1,n):
    D=gcd(D,li[i])
print(D)