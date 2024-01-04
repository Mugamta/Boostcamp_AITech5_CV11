"""
https://www.acmicpc.net/problem/1302

가장 많이 팔린 책의 제목 - 카운팅 - 인덱싱 필요
책의 제목은 문자열 - 해싱 필요
따라서 해시 문제로 판별하여 풀이 시작

11:22 문제 읽기 시작
11:23 코드 작성 시작
11:27 제출 - 틀렸습니다  -> 가장 많이 팔린 책 조건을 읽지 않음
11:28 수정 제출 - 정답

"""

import sys


def fun():
    N = int(sys.stdin.readline())
    d = dict()
    for i in range(N):
        s = sys.stdin.readline()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1

    max_book_cnt = 0
    max_book = ""

    for key in d:
        if d[key] > max_book_cnt:
            max_book_cnt = d[key]
            max_book = key
        elif d[key] == max_book_cnt:
            if max_book > key:
                max_book = key

    return max_book


print(fun())
