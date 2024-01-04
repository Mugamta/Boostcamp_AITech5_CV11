def main():
    
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(key= abs, reverse=True)

    MIN = 2000000000
    for index in range(len(arr)-1):
        if MIN > abs(arr[index]+arr[index+1]):
            MIN = abs(arr[index]+arr[index+1])
            result = [arr[index], arr[index+1]]
    
    result.sort()
    print(result[0], result[1])
        
    return 0


if __name__ == '__main__':
    main() 