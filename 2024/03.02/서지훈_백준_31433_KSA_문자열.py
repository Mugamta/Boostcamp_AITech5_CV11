def func():
    X = input()

    # 결국 문자열을 만들 때, KSA의 순서를 유지하지 않는 문자열은 지워야 한다.
    # 하지만 SAKSA와 같이 앞 문자에 K를 붙이는 것이 이득이 있고
    # KSA와 같이 문자열을 그대로 시작하는 것이 이득인 경우가 있다.
    # 따라서 세 가지 경우로 나누어 만든다.

    chars = ['K', 'S', 'A']

    length = len(X)
    res = 2 * length  # 모든 문자를 지우고 새로 작성하는 경우의 수이므로 이보다 클 수 없음

    # 1. 현재 문자열에서 KSA를 그대로 만들기
    idx, tmp = 0, 0
    for i in range(length):
        if X[i] == chars[idx % 3]:
            idx += 1
        else:
            tmp += 1  # KSA의 순서와 다르다면 지워야 함
    # KSA와 어긋나는 순서만큼 지웠으므로, 이제 새로운 문자를 추가해야함
    # 이는 idx (순서에 맞는 문자의 길이)와 원본 문자열의 길이의 차이와 같음
    res = min(res, tmp + abs(idx - length))

    # 2. 앞 문자에 K 추가하기
    KX = 'K' + X
    idx, tmp = 0, 1  # K를 추가했으므로 한 문자를 지워야 함
    for i in range(length + 1):
        if KX[i] == chars[idx % 3]:
            idx += 1
        else:
            tmp += 1
    res = min(res, tmp + abs(idx - length))

    # 3. 앞 문자에 KS 추가하기
    KSX = 'KS' + X
    idx, tmp = 0, 2  # KS를 추가했으므로 뒤 두 문자를 지워야 함
    for i in range(length + 2):
        if KSX[i] == chars[idx % 3]:
            idx += 1
        else:
            tmp += 1
    res = min(res, tmp + abs(idx - length))

    print(res)


func()
