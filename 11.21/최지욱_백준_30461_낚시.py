import sys

def main():
    
    row, col, n = map(int, sys.stdin.readline().rstrip().split())
    
    lake = []
    
    for _ in range(row):
        lake.append(list(map(int, sys.stdin.readline().rstrip().split())))
        
    for c in range(col):
        total = 0 
        for r in range(row):
            total += lake[r][c]
            lake[r][c]= total
            
    for c in range(1, col):
        for r in range(1, row):
            lake[r][c] += lake[r-1][c-1]
             
    for _ in range(n):
        r, c = map(int, sys.stdin.readline().rstrip().split())
        print(lake[r-1][c-1])
        
main()