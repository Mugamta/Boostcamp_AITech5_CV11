'''
A + B + C + D + E + F + G
A + B -(C + D + E + F + G)
A + B - C -(D + E)-(F + G)

첫 번재 '-' 기호를 기준으로 선행하는 부분은 합으로 이루어질 수 밖에 없음
후행하는 부분은 괄호를 이용하여 모두 음의 값으로 만들때 최솟값을 가짐
'''



def main():
    
    string = input()
    arr = string.split('-')     ## 첫 - 부호로 head와 tail을 분리
    
    head = list(map(int, arr[0].split('+'))) ## head 부분 +로 모두 분리
    tail = [sum(list(map(int,i.split('+')))) for i in arr[1:]]     ## -로 분리된 각 리스트들을 한번 더 +로 분리하고 sum을 구함
    
    print(sum(head)-sum(tail))      ## head의 모든 숫자의 합에서 tail의 모든 숫자의 합을 빼기
    
main()



