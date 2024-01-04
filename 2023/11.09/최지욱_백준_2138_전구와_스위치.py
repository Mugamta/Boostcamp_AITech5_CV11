def check_case(case1, target, n):
    cnt = 0
    for i in range(0, n - 2):
        if case1[i] != target[i]:
            case1[i] = abs(case1[i] - 1)
            case1[i + 1] = abs(case1[i + 1] - 1)
            case1[i + 2] = abs(case1[i + 2] - 1)
            cnt += 1
    if (case1[-2] != target[-2]) and (case1[-1] != target[-1]):
        cnt += 1
    elif (case1[-2] == target[-2]) and (case1[-1] == target[-1]):
        pass
    else:
        cnt = -1
    return cnt

def main():
    n = int(input())
    start = [int(i) for i in input()]
    target = [int(i) for i in input()]
    
    case1 = start.copy()
    case2 = start.copy()
    case2[0] = abs(case2[0] - 1)
    case2[1] = abs(case2[1] - 1)
    
    result1 = check_case(case1, target, n)
    result2 = check_case(case2, target, n)
    
    if result1 == -1 and result2 == -1:
        print(-1)
    elif result1 == -1:
        print(result2 + 1)
    elif result2 == -1:
        print(result1)
    else:
        print(min(result1, result2 + 1))

main()