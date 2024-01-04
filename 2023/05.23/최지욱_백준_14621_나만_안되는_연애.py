def main():

    N, M = map(int, input().split(' '))
    unis = list(input().split(' '))
    
    edges = []
    
    for _ in range(M):
        p1, p2, cost = map(int, input().split(' '))
        edges.append([cost, p1, p2])
        
    edges.sort()
      
    groups = [{i} for i in range(N)]
    net_cost =0 
    
    for edge in edges:
        cost, p1, p2 = edge
        
        if unis[p1-1]== unis[p2-1]:
            continue
        
        if groups[p1-1] == groups[p2-1]:
            continue
        
        new_group = groups[p1-1].union(groups[p2-1])
        
        for elem in new_group:
            groups[elem] = new_group
            
        net_cost += cost
        
    if len(new_group)==N:
        print(net_cost)
    else:
        print(-1)            
            
main()