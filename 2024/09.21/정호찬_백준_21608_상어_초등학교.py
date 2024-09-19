"""
메모리 : 31120 KB
시  간 : 152 MS
"""

import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def main():
    N = int(input().strip())
    class_room = [[0] * (N) for _ in range(N)]

    # 좋아하는 사람 4명 
    likes_sheet = {}
    for i in range(1, (N**2) + 1):
        likes_member = list(map(int, input().split()))
        likes_sheet[likes_member[0]] = likes_member[1:]


    # 학생 자리 정하기
    for k, v in likes_sheet.items():
        likes_member = v
        tmp = []
        for r in range(N):
            for c in range(N):
                if class_room[r][c] == 0: # 비어 있다면
                    like, empty = 0, 0 #좋아하는 학생수, 비어있는 자리 수

                    for idx in range(4): # 거리 한칸씩 이동 하면서 체크
                        nr, nc = r + dr[idx], c + dc[idx]

                        if 0 <= nr < N and 0 <= nc < N:

                            # 이동한 자리가 좋아하는 멤버라면
                            if class_room[nr][nc] in likes_member:
                                like += 1
                            # 이동한 자리가 비어있는 자리라면
                            if class_room[nr][nc] == 0:
                                empty += 1
                    # 좋아하는 사람, 비어있는, 좌표 기준으로 저장
                    tmp.append([like, empty, r, c])
        # 다돌고 4개의 기준을 적용하여 정렬
        tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
        # 가장 높은 스코어의 자리에 학생 자리 배정
        class_room[tmp[0][2]][tmp[0][3]] = k

    # 만족도 구하기
    score = 0
    for r in range(N):
        for c in range(N):
            student = class_room[r][c]
            num_of_likes = 0
            for idx in range(4):
                nr, nc = r + dr[idx], c + dc[idx]

                if 0 <= nr < N and 0 <= nc < N:
                    # 좋아하는 학생 수
                    if class_room[nr][nc] in likes_sheet[student]:
                        num_of_likes += 1
            # 인접한 좋아하는 학생수 기준으로 스코어 갱신
            if num_of_likes != 0:
                score += (10 ** (num_of_likes - 1))

    print(score)
if __name__ == '__main__':
    main()