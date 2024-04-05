n = int(input())
thr, thr_idx = 0,0 #최대값, 최대값 인덱스
dp = [0]*(1001)
max_x = 0
for _ in range(n):
  l, h = map(int, input().split())
  dp[l] = h
  if h> thr:
    thr = h
    thr_idx = l
  if max_x < l: #x좌표 최대
    max_x = l
    
tmp_max=0
ans = 0
for i in range(thr_idx+1): #최대값까지
  tmp_max = max(tmp_max, dp[i])
  ans += tmp_max

tmp_max = 0
for i in range(max_x, thr_idx, -1):#거꾸로 최대까지
  tmp_max = max(tmp_max, dp[i])
  ans += tmp_max

print(ans)
