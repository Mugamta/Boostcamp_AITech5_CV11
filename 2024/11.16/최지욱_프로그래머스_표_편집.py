'''
메모리 : 221MB
시간 : 695.64ms
'''

def solution(n, k, cmd):
    ## double linked list 활용
    double_linked = [[i - 1, i, i + 1] for i in range(n)]
    
    ## set head, tail
    double_linked[0][0] = None  
    double_linked[n - 1][2] = None  
    
    stack = []
    result = ["O"] * n

    for command in cmd:
        if command == "C":
            stack.append(k)
            result[k] = 'X'
            
            p, c, n = double_linked[k]
            if p is not None:
                double_linked[p][2] = n
            if n is not None:
                double_linked[n][0] = p
            
            if n is not None:
                k = n
            else:
                k = p

        elif command == "Z":
            i = stack.pop()
            result[i] = 'O'
            
            p, c, n = double_linked[i]
            if p is not None:
                double_linked[p][2] = i
            if n is not None:
                double_linked[n][0] = i

        else:
            direction, num = command.split()
            num = int(num)
            
            for _ in range(num):
                if direction == "U":
                    k = double_linked[k][0]
                elif direction == "D":
                    k = double_linked[k][2]

    return "".join(result)