def main():

    string = input()
    length = len(string)
    
    num = 1
    index =0
    
    while index<length:
        for t in str(num):
            if index>=length:
                break
            if string[index]==t:
                index+=1
        num += 1
                    
    print(num-1)
    return 0


if __name__ == '__main__':
    main()
