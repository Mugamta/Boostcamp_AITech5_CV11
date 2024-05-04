n = int(input()) # 스위치 개수
swi = list(map(int, input().split())) # 스위치 상태
m = int(input()) # 학생 수

for _ in range(m):
    a, b = map(int, input().split()) # 성별, 받은 숫자
    if a == 1: # 남자
        for i in range(b-1, n, b): # 번호의 배수
            swi[i] = 1 if swi[i] == 0 else 0 # 상태 변경
    else: # 여자
        b -= 1 # 입력 숫자를 0부터 시작하는 인덱스로 변경
        left = b
        right = b
        while left >= 0 and right < n and swi[left] == swi[right]: # 좌우 대칭 확인
            left -= 1
            right += 1
        left += 1
        right -= 1
        for i in range(left, right+1): # 대칭 부분 상태 변경
            swi[i] = 1 if swi[i] == 0 else 0

# 20개씩 출력
for i in range(n):
    print(swi[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
