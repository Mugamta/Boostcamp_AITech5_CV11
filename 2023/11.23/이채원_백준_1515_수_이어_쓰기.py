s = input()

N = 0
while len(s) > 0 :
    N += 1
    n_s = str(N)
    n_lst = list(n_s)
    for i in n_lst :
        if len(s)>0 and s[0] == i :
            s = s[1:]
    
print(N)