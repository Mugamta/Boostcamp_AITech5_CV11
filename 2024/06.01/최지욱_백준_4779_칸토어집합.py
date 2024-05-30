'''
메모리 : 32676KB
시간 : 48ms
'''

import sys

def process(string):
    
    length = len(string)
    if length==1:
        return "-"
    else:
        return process("-"*(length//3))+" "*(length//3)+process("-"*(length//3))

def main():
    
    input_data = sys.stdin.readlines()
    
    for i in input_data:
        print(process(3**int(i)*"-"))
    
    return 0


if __name__ =='__main__':
    main()