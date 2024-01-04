"""
21:27 문제 읽기 시작
프로젝트 팀을 만드는 문제... 유니온 파인드?
s1 -> s2... sr -> s1의 식으로 사이클을 이뤄야 함 - 유니온 파인드 가능
혹은 dfs로 1번 -> 선택한 번호 -> ...의 흐름에서 자기 자신으로 돌아오는지로 판별 가능

21:34 유니온 파인드 구현 시작
21:38 구현 도중 든 생각 - 1 -> 2 -> 3 -> 2의 흐름이라면 unionfind는 루트만 판별하므로 (2, 3)만 묶어내려면 find 도중 조건 필요
그걸 감안하면 dfs로 구현하는게 더 편할듯?
21:40 dfs 구현 시작
10:15 첫 제출 - 시간 초과
	원인은 list대신 deque를 사용한 것
10:24 수정 제출 - 정답
"""

import sys
sys.setrecursionlimit(1000000)


def dfs(idx):
    """
    1 -> 2 -> 3 -> 4 -> 2
    1 -> 3 -> 4 -> 1
    1 - > 3 -> 3
    """

    if visited[idx]:  # 이미 방문한 학생이 있다는 것은 내부에 사이클이 형성되거나/다른 사람을 선택한 학생
        length = len(visit)

        tmp = 0

        for j in range(length-1, -1, -1):  # students[idx]와 동일한 지점을 찾을때까지 거슬러 올라감
            tmp += 1
            if visit[j] == idx:
                global result
                result -= tmp
                break
        return

    visited[idx] = True
    visit.append(idx)
    dfs(students[idx])


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    students = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (n+1)
    result = n

    for i in range(1, n + 1):
        if not visited[i]:
            if i == students[i]:  # 자기 자신을 팀으로 가르키는 경우
                result -= 1
            elif not visited[i] and not visited[students[i]]:  # 학생과 다음 학생이 방문 가능하다면 탐색 시작
                visit = []
                dfs(i)

        visited[i] = True

    sys.stdout.write(str(result))
    sys.stdout.write("\n")
