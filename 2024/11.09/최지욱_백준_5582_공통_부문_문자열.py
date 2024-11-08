"""
메모리 : 236272KB
시간 : 412ms
"""
def main():
    string1 = input()
    string2 = input()

    n = len(string1)
    m = len(string2)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    MAX = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                MAX = max(MAX, dp[i][j])
            else:
                  dp[i][j] = 0 
    print(MAX)

if __name__ == '__main__':
    main()