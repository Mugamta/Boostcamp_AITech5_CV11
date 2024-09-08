def main():
    N = int(input()) 

    fibo_people = [1, 2]        ## N인
    fibo_chicken = [1, 1]       ## M닭

    ## 피보나치 생성
    while fibo_people[-1] <= N:
        fibo_people.append(fibo_people[-1] + fibo_people[-2])
        fibo_chicken.append(fibo_chicken[-1] + fibo_chicken[-2])

    dp_min = [100000000 for _ in range(N + 1)]
    dp_min[0] = 0
    
    ## 인원 수
    for i in range(1, len(fibo_people)):
        for j in range(1, N + 1):
            
            ## j명의 사람에게 주는 최소한의 치킨 수 dp[j]에서 
            ## i명분의 치킨을 fibo_chicken에 해당하는 치킨수로 대체한 값 중 더 작은 수
            dp_min[j] = min(dp_min[j], dp_min[j - fibo_people[i]] + fibo_chicken[i])

    dp_max = [0 for _ in range(N + 1)]

    for i in range(1, len(fibo_people)):
        for j in range(fibo_people[i], N + 1):
            dp_max[j] = max(dp_max[j], dp_max[j - fibo_people[i]] + fibo_chicken[i])

    print(dp_min[N], dp_max[N])

if __name__ == "__main__":
    main()