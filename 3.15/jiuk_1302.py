num = int(input())
    
count = dict()
    
for i in range(num):
    name = input()
    if name in count.keys():
        count[name] += 1
    else:
        count[name] = 1
    
MAX = max(count.values())
    
result =[]
for t in count:
    if count[t] == MAX:
        result.append(t)
        
print(sorted(result)[0])
