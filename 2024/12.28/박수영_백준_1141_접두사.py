import sys
from collections import deque
input = sys.stdin.readline

def solution(n, words):
    not_prefix_set = []

    # 길이, 사전 순서대로 정렬 후 큐로 변환
    words.sort(key=lambda x: (len(x), x))
    words = deque(words)

    while words:
        word = words.popleft()

        # 현재 단어와 남은 단어 간 접두사 판별
        is_prefix = False
        for another_word in words:
            if another_word.startswith(word):
                is_prefix = True
                break
        
        # 접두사가 아니면 집합에 추가
        if not is_prefix:
            not_prefix_set.append(word)

    return len(not_prefix_set)
    

def main():
    N = int(input())
    words = [input().strip() for _ in range(N)]

    res = solution(N, words)
    print(res)


if __name__ == "__main__":
    main()
