import sys

def main() :
    A, B, N = map(int, sys.stdin.readline().split())

    answer = ''

    #두자리수 소수 
    # 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

    if B//10 not in [1,3,7,9] :
        return "-1"
      
    # a1 = A%10 # 1, 3, 7, 9

    if A%10 == 9 :
        answer += str(A)
        answer += "7"
        answer += "1"*(N-5)
        answer += str(B)
        return answer
    else :
        answer += str(A)
        answer += '1'*(N-4)
        answer += str(B)
        return answer
answer = main()    
print(answer)