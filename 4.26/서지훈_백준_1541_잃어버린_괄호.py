expr = input()
expr_len = len(expr)

result = 0  # 결과 값
start, end = 0, 0  # 숫자의 시작, 끝을 표기
idx = 0
while idx <= expr_len:
    if idx == expr_len or expr[idx] == '+':
        result += int(expr[start:end])
        idx += 1
        start, end = idx, idx
        continue

    elif expr[idx] == '-':
        result += int(expr[start:end])
        idx += 1
        start, end = idx, idx
        break

    end += 1
    idx += 1

while idx <= expr_len:
    if idx == expr_len or expr[idx] == '-' or expr[idx] == '+':
        result -= int(expr[start:end])
        idx += 1
        start, end = idx, idx
        continue
    end += 1
    idx += 1

print(result)