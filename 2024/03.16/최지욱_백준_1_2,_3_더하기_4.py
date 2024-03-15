def main():
    n = int(input())
    
    for _ in range(n):
        t = int(input())
        
        total = 0
        for i in range(0,t+1,3):
            cnt = ((t-i)//2)+1
            total += cnt
        
        print(total)
    return 0


if __name__ == '__main__':
    main() 
    
