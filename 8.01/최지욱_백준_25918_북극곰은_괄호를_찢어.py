def main():
    N = int(input())
    string  = input()
    
    num =0
    arr=[]
    
    for letter in string:
        if letter=='(':
            num += 1
            arr.append(num)
        elif letter==')':
            num -= 1
            arr.append(num)
    
    if arr[-1]==0:
        print(max([abs(i) for i in arr])) 
    else:
        print(-1)
main()