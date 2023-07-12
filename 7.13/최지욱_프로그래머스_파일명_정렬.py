def solution(files):
    
    num = '0123456789'
    result = []
    
    for order,file in enumerate(files):
        name =[]
        for i in range(len(file)):
            if file[i] not in num and file[i+1] in num:
                name.append(file[:i+1].lower()) ### head
                char = i+1

            if file[i] in num and len(file)==i+1:
                name.append(int(file[char:i+1])) ### number
                name.append(order)
                name.append('') ##tail
                name.append(file)
                result.append(name)
                break

            if file[i] in num and file[i+1] not in num:
                name.append(int(file[char:i+1])) ### number
                name.append(order)
                name.append(file[i+1:]) ### tail
                name.append(file)
                result.append(name)
                break

    return [i[4] for i in sorted(result)]