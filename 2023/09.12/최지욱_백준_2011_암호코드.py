def main():
    
    string = input()
    
    arr = [1 ,1]
    if string[0]=='0':
        print(0)
        return 0
    
    for i in range(len(string)-1):
        if string[i:i+2] in ['00','30','40','50','60','70','80','90']:
            print(0)
            return 0
        elif string[i]=='0':
            arr.append(arr[i+1]%1000000)
        elif string[i+1]=='0':
            arr.append(arr[i]%1000000)
        elif int(string[i:i+2]) < 27:
            arr.append((arr[i]+arr[i+1])%1000000)
        else:
            arr.append(arr[i+1]%1000000)
    
    print(arr[-1]%1000000)
    
main()