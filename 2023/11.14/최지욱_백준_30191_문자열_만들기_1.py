def main():
    
    n = int(input())
    arr = [-1 if i=='S' else 1 for i in input()]
    result = ''

    prev_status = 0
    
    for i in arr[::-1]:
        status = prev_status + i
        if abs(status) > abs(prev_status):
            if i == -1:
                result += 'UN'
            else:
                result += 'SN'
        else:
            result += 'N'
            
        prev_status = status
            
    print(len(result))
    print(result)    

main()