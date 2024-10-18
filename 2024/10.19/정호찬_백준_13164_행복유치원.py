"""
현재 키 순서대로 오름 차순으로 정렬된 배열이 들어온다

이말은 조를 만드는 비용은 연속된 합이라는 것을 의미한다.
따라서 현재 K개의 조를 만들어야하는데, 이것은 K - 1 만큼 큰 차를 제거할 수 있음을 의미한다

즉, 각 인접한 차를 구하고 이를 내림차순으로 정렬한다음
K - 1 부터 끝까지의 합을 출력하면 총합이 된다

메모리 : 66600 KB
시  간 : 252 MS
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
array = list(map(int, input().split()))

diff_array = []
for i in range(N - 1):
    diff_array.append(array[i + 1] - array[i])

diff_array  = sorted(diff_array , reverse=True)
print(sum(diff_array[K - 1:]))