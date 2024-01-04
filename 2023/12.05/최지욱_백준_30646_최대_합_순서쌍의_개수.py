def main():
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    MAX = 0
    result = dict()
    accum = [0]
    total = 0 
    
    for index, i in enumerate(arr):
        total += i 
        accum.append(total)
        
        if i in result:
            result[i][1] = index
        else:
            result[i] = [index, index]

    count =0 
    for num in result:
        i, j = result[num]
        val = accum[j+1] - accum[i]
        if val > MAX:
            MAX =val
            count = 1
        elif val ==MAX:
            count += 1
        else:
            continue
    
    print(MAX, count)
    return 0


if __name__ == '__main__':
    main()