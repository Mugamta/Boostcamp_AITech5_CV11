import sys

def main():
    
    arr = [0] + [1]*1000000
    
    for i in range(2, 1000001):
        for t in range(i, 1000001, i):
            arr[t] += i
    
    for i in range(1, 1000001):
        arr[i] += arr[i-1]

    T = int(input())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        print(arr[n])

    return 0


if __name__ == '__main__':
    main() 