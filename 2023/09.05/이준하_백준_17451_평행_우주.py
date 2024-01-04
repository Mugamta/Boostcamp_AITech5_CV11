n = int(input())
vs = list(map(int,input().split()))
v = vs[-1]

for i in range(n-2, -1, -1):                    # 뒤에서 두번째부터 역순으로
    if vs[i] > v:                         # speed보다 행성 속력이 크다면
        v = vs[i]                         # speed를 현재 행성 속력으로 업데이트
    else:                                       # speed가 더 크거나 작다면
        if v%vs[i]:                       # 정수배가 되지 않는다면 
            v = (v//vs[i]+1) *vs[i] # 배수이면서 최소값으로 업데이트
print(v)