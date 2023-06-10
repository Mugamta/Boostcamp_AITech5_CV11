def main():

    N, X = map(int, input().split())
    arr= list(map(int, input().split()))
    
    prev = MAX = sum(arr[:X])
    NUM = 1
    
    for i in range(N-X):
        new = prev-arr[i]+arr[i+X]
        
        if MAX < new:
            MAX = new
            NUM = 1
        elif MAX == new:
            NUM += 1
        else:
            pass
        prev = new
    
    if MAX==0:
        print('SAD')
    else:
        print(MAX)
        print(NUM)


main()