def main():
    
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        
        row1 = list(map(int, input().split(' ')))
        row2 = list(map(int, input().split(' ')))
        
        row1_1, row1_2 = 0, 0
        row2_1, row2_2 = 0, 0
        
        for i in range(n):
            
            row1[i] = max(row2_1, row2_2) + row1[i]
            row2[i] = max(row1_1, row1_2) + row2[i]
            
            
            row1_1 = row1_2
            row1_2 = row1[i]
  
            row2_1 = row2_2
            row2_2 = row2[i]
        
            
        
        print(max(row1[-1], row2[-1]))
        
    
    

main()