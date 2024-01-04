import sys
input = sys.stdin.readline
def cul():
    string = input()
    try:
        string = string.split('-')
    except:
        return sum(map(int, string.split('+')))
    first = sum(map(int,string[0].split('+')))
    second = sum([sum(map(int,i.split('+'))) for i in string[1:]])
    return first-second
print(cul())