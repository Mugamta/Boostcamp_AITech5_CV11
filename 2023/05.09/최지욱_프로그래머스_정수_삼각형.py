def solution(triangle):

    up = triangle[0]
    
    for arr in triangle[1:]:
        for t in range(len(arr)):
            if t==0:
                arr[t] = up[t]+arr[t]
            elif t==len(arr):
                arr[t] = up[t-1]+arr[t]
            else:
                arr[t] = max(up[t-1:t+1]) + arr[t]       
        up = arr

    return max(arr)