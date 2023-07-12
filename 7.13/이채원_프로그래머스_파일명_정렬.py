def solution(files):
    words = []
    for f in files :

        head = ''
        number = ''
        tail = ''
        
        for i in range(len(f)) :
            if f[i].isdigit() :
                head = f[:i]
                number = f[i:]
                for j in range(len(number)) :
                    if not number[j].isdigit() :
                        tail = number[j:]
                        number = number[:j]
                        break
                break
        words.append([head, number, tail])
                        
        
    words.sort(key = lambda x : (x[0].lower(),int(x[1])) )
    answer = list(''.join(x) for x in words)
    return answer