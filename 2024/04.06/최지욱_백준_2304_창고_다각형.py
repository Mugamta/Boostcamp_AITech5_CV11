def main():
    
    n = int(input())
    arr = []
    
    for _ in range(n):
        loc, h = map(int, input().split())
        arr.append([h, loc])
    
    arr.sort(reverse=True)
    MAX_h, MAX_loc = arr[0]
    MIN_loc = MAX_loc
    area = MAX_h
    
    for h, loc in arr[1:]:
        
        if loc<MIN_loc:
            area += (h*(MIN_loc-loc))
            MIN_loc=loc
        elif loc>MAX_loc:
            area += (h*(loc-MAX_loc))
            MAX_loc= loc
        else:
            pass
            
    print(area) 
    return 0


if __name__ == '__main__':
    main()