def main():
    
    string = input()
    arr = string.split('-')     ## 첫 - 부호로 head와 tail을 분리
    
    head = list(map(int, arr[0].split('+'))) ## head 부분 +로 모두 분리
    tail = [sum(list(map(int,i.split('+')))) for i in arr[1:]]     ## -로 분리된 각 리스트들을 한번 더 +로 분리하고 sum을 구함
    
    print(sum(head)-sum(tail))      ## head의 모든 숫자의 합에서 tail의 모든 숫자의 합을 빼기
    
main()
