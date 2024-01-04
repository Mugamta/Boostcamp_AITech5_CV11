def solution(p):
    
    ##############Encoding phase##############
    arr =[]
    for t in p:                 ## 괄호를 -1, 1로 치환
        if t=='(':
            arr.append(1)
        else:
            arr.append(-1)
    ##########################################
    
    
    ##############Decoding phase##############
    string = ''
    for num in do(arr):         ## do를 실행한 arr 리스트 decoding
        if num==1:
            string += '('
        else:
            string += ')'
    ##########################################

    return string 


def split(arr):
    accum = 0 
    for index, i in enumerate(arr):
        accum += i
        if accum == 0:                      ## 여는 괄호('(')의 수보다 닫는 괄호(')')의 수가 같아지는 지점 
            break               
    return arr[:index+1], arr[index+1:]     ## 같아지는 지점에서 균형잡힌 괄호 문자열 u, v로 분리


def correct(arr):                           ## 올바른 괄호 문자열 체크
    accum =0
    for index, i in enumerate(arr):     
        accum += i
        if accum <0:                        ## 여는 괄호('(')의 수보다 닫는 괄호(')')의 수가 더 많은 경우 
            return False                    ## 올바르지 않은 괄호 문자열
        
    return True                             ## 그렇지 않은 경우 올바른 괄호 문자열
        
def do(arr):
    if arr==[]:                             ## 1. 빈 문자열인 경우
        return []                           ##    그대로 반환
    u, v = split(arr)                       ## 2. u,v split
    if correct(u):                          ## 3. u가 올바른 괄호 문자열인 경우 
        return u + do(v)                    ##    3-1. u에 수행한 결과 do(v)를 이어 붙이고 반환
    else:                                   ## 4. 문자열 u가 올바른 괄호 문자열이 아닌 경우
        new_arr = [1] + do(v) + [-1]            ## 4-1 / 4-2 / 4-3
        return new_arr + [-i for i in u[1:-1]]  ## 4-4 / 4-5 / (뒤집어서 붙이기)
        