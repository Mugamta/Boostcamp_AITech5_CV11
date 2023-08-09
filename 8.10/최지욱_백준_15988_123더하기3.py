def main():
    arr= [1,2,4]
    for _ in range(1000000):
        arr.append(sum(arr[-3:])%1000000009)
    
    num = int(input())
    for _ in range(num):
        index = int(input())
        print(arr[index-1])
    
main()



'''

1 | 1

2 | 1 + 1
    2

3 | 1 + 1 + 1
    1 + 2
    2 + 1
    3

    
4 | 1 +(3)              --- N(1)         

    1 + 1 +(2)          --- N(2)
    2 +(2)
    
    1 + 1 + 1 +(1)      --- N(3)
    1 + 2 +(1)
    2 + 1 +(1)
    3 +(1)

5 | N(2)
    N(3)
    N(4)

K | N(k-3)
    N(k-2)
    N(k-1)

'''