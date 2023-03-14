import sys

arr =[]
num = int(input())

    
for i in range(num):
    x,y = map(int, sys.stdin.readline().split())
    arr.append([x,y])


value = 0

length = len(arr)

for i in range(length):
    two = arr.copy()
    two.pop(i)
    origin_x,origin_y = arr[i][0],arr[i][1]
    for j in range(length-2):
        vector1_x, vector1_y = two[j][0]-origin_x, two[j][1]-origin_y
        
        for k in range(j+1, length-1):
            vector2_x, vector2_y = two[k][0]-origin_x, two[k][1]-origin_y
            if vector1_x*vector2_x == - vector1_y*vector2_y:

                value +=1


print(value)
