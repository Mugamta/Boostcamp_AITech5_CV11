import sys



def gcd(a, b) : 
    while b :
        mod = b 
        b = a%b
        a = mod
    return a


N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A = list(abs(i - S) for i in A)
# A.sort()

d = min(A)

for i in range(len(A)) :
    d = gcd(A[i], d)


print(d)
