"""
메모리 : 32412KB
시간 : 40ms
"""
def main():

    N = int(input())
    arr = []
    
    for _ in range(N):
        arr.append(input())
    
    arr.sort()
    
    '''
    정렬 시, 직전의 선행하는 단어가 직후의 후행하는
    단어의 접두어가 될 수 있음. 이를 이용하여 반복문 구현.
    '''
    prev = ""
    result = 1
    for word in arr:
        if len(word) < len(prev):
            result += 1
        else:
            for i in range(len(prev)):
                if word[i] != prev[i]:
                    result += 1
                    break
        prev = word
        
    print(result)   
    return 0
    
if __name__ == '__main__':
    main()
