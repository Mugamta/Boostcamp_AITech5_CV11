import sys
input = sys.stdin.readline

def solution(n, arr):
    """
    time: 30m 33s
    완전탐색
    - 1번 주사위의 위치를 정하면, 나머지 주사위의 위치는 규칙에 따라 고정됨
    """
    # 마주 보는 면의 인덱스 정보
    see_each_other = {
        0: 5, 1: 3, 2: 4,
        3: 1, 4: 2, 5: 0
    }

    answer = float('-inf')

    # 1번 주사위의 윗면 선택
    for top_idx in range(6):
        top = arr[0][top_idx]

        # 마주보는 면의 인덱스 정보 및 숫자 가져오기
        bot_idx = see_each_other[top_idx]
        bot = arr[0][bot_idx]

        # 윗면과 아랫면을 잠시 0으로 처리
        arr[0][top_idx] = 0
        arr[0][bot_idx] = 0

        # 옆면 중 최댓값을 누적
        max_sum_of_side_area = max(arr[0])

        # 원래 값으로 복원
        arr[0][top_idx] = top
        arr[0][bot_idx] = bot

        # 2번 주사위부터 쌓기
        for dice_num in range(1, n):
            # 같은 숫자의 위치 찾기
            bot_idx = arr[dice_num].index(top)
            bot = top

            # 마주보는 면의 인덱스 정보 및 숫자 가져오기
            top_idx = see_each_other[bot_idx]
            top = arr[dice_num][top_idx]

            # 윗면과 아랫면을 잠시 0으로 처리
            arr[dice_num][top_idx] = 0
            arr[dice_num][bot_idx] = 0

            # 옆면 중 최댓값을 누적
            max_sum_of_side_area += max(arr[dice_num])

            # 원래 값으로 복원
            arr[dice_num][top_idx] = top
            arr[dice_num][bot_idx] = bot

        # 최댓값 갱신
        if max_sum_of_side_area > answer:
            answer = max_sum_of_side_area

    return answer


def main():
    # 입력
    n_dice = int(input())
    dice_list = [list(map(int, input().split())) for _ in range(n_dice)]

    # 함수 호출
    res = solution(n_dice, dice_list)

    # 결과 출력
    print(res)


if __name__ == "__main__":
    main()
