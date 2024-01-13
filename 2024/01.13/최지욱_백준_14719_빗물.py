def main():
    
    height, width = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))

    blocks = [[1 for _ in range(width)] for _ in range(height)]

    ## create blocks
    for index, i in enumerate(arr):
        for h in range(i):
            blocks[h][index]=0
    
    ## forward fill
    for h in range(height-1,-1,-1):
        i=0
        while (blocks[h][i]) & (i<width-1):
            blocks[h][i] =0
            i += 1
    
    ## backward fill
    for h in range(height-1,-1,-1):
        i=width-1
        while (blocks[h][i]) & (i>=0):
            blocks[h][i] =0
            i -= 1
    
    ## print sum
    print(sum([sum(row) for row in blocks]))
    
    return 0


if __name__ == '__main__':
    main() 
