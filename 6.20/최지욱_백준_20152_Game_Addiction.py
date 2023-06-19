def main():
    a,b =map(int , input().split())
    d = abs(a-b)
    arr=[1]
    
    if d==0:
        print(1)
        return 0
    
    for _ in range(d):
        t = [1]
        prev = 1
        for i in arr[1:]:
            prev += i
            t.append(prev)
        t.append(prev)
        arr = t
            
    print(t[-1])  
    
main()
