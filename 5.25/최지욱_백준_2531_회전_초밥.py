def main():
    n, d, k, c = map(int, input().split(' '))
    arr = [int(input()) for _ in range(n)]
    
    arr = arr+arr
    
    counter = {}
    for i in range(k):
        
        if arr[i] in counter:
            counter[arr[i]] = counter[arr[i]] + 1
        else:
            counter[arr[i]] = 1
    
    MAX = len(counter) + (c not in counter) 
    
    for i in range(n):
        counter[arr[i]] -= 1
        if counter[arr[i]] == 0:
            del counter[arr[i]]
        
        if arr[i+k] in counter:
            counter[arr[i+k]] = counter[arr[i+k]] + 1
        else:
            counter[arr[i+k]] = 1
        
        MAX = max(MAX, len(counter) + (c not in counter))
    
    print(MAX)
    
main()