def solution(triangle):
    DPlist = [triangle[0]]
    
    for i,lst in enumerate(triangle):
        if i == 0:
            continue
        col = []
        col_len = len(lst)-1
        for j,k in enumerate(lst):
            if j == 0:
                col.append(DPlist[i-1][0]+k)
            elif j == col_len:
                col.append(DPlist[i-1][col_len-1]+k)
            else:
                col.append(max(DPlist[i-1][j],DPlist[i-1][j-1])+k)
        DPlist.append(col)
    return max(DPlist[-1])