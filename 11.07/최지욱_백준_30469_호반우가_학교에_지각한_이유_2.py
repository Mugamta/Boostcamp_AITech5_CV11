def main():
    
    prime_dict = dict()
    
    for n in range(1,10):
        prime_dict[str(n)]= []
        
    
    for i in range(11, 98):
        PRIME = True
        
        for t in range(2,10,1):
            if i%t==0:
                PRIME = False
                break
        
        if PRIME:
            prime_dict[str(i//10)].append(str(i%10))
            
    
    a, b, n = input().split()
    n = int(n)
    
    if a[1] in prime_dict[a[0]] and b[1] in prime_dict[b[0]] and (b[0] in ['1','3','7','9']):
        pass
    else:
        print(-1)
        return 0
    
    
    ## 새로운 풀이
    
    if a[1]=='9':
        print(a + '7' + '1'*(n-5) + b)
    else:
        print(a + '1'*(n-4) + b)
    
    
    
    ## 시간 초과 풀이

    # arr = [a]
    
    # while arr:
    #     target = arr.pop()
        
    #     if len(target)>n-1:
    #         continue
        
    #     if len(target)==n-1 and target[-1]==b[0]:
    #         print(target+b[1])
    #         return 0
        
        
    #     for num in prime_dict[target[-1]]:
    #         arr.append(target+num)
            
        
    # print(-1)
    # return 0
                
main()