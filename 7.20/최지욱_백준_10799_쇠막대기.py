def main():
    stack = []
    total_num = 0
    
    string = input()

    for i in range(len(string)):
        if string[i] == '(':        #  ( 인 경우 새로운 막대기
            stack.append(i)         # stack에 index i 추가
        else:                       #  ) 인 경우 1,2
            if stack[-1] == i - 1:  # 1. 레이저인 경우
                stack.pop()         # 직전 ( 무시
                total_num += len(stack)
            else:                   # 2. 막대기의 끝인 경우
                stack.pop()         # 최근 막대기 pop
                total_num += 1      # 해당 조각 추가

    print(total_num)

main()