import sys
def change(s) :
    if s=='0' :
        return '1'
    else :
        return '0'
def switch() :
    N = int(input())
    ip = input()
    b = list(input())
    a1 = list(ip)
    a2 = list(ip)
    sw=[0,0,1,1]
    for i in range(2) :
        a2[i] = change(a2[i])
    for i in range(N-2) :
        if a1[i] != b[i] :
            a1[i] = change(a1[i])
            a1[i+1] = change(a1[i+1])
            a1[i+2] = change(a1[i+2])
            sw[0]+=1
        if a2[i] != b[i] :
            a2[i] = change(a2[i])
            a2[i+1] = change(a2[i+1])
            a2[i+2] = change(a2[i+2])
            sw[2]+=1
    a = [a1[-2:],[change(a1[-2]), change(a1[-1])],a2[-2:],[change(a2[-2]), change(a2[-1])]]
    b = b[-2:]
    # print(a[0])
    # print(b)
    sw[1]=sw[0]+1
    sw[3]=sw[2]+1
    for i in range(4) :
        if a[i][0]==b[0] and a[i][1]==b[1] : return sw[i]

    return -1

print(switch())

