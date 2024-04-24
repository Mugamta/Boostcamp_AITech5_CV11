def main():
    
    N = int(input())
    arr = list(map(int, input().split()))
       
    total = 0
    arr.sort()
    t = 1
    while arr:
        total += arr.pop()*t
        t += 1
    
    print(total)
    return 0


if __name__ == '__main__':
    main() 
    