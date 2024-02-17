from collections import deque

def main():
    
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        x,y = map(int, input().split())
        queue= deque([[x,y]])
        stores = [list(map(int, input().split())) for _ in range(n)]
        visited = [False for _ in range(n)]
        
        d_x, d_y = map(int, input().split())

        festival =False
        
        while queue:
            x,y = queue.popleft()
            if abs(x-d_x)+abs(y-d_y)<=1000:
                festival = True
                break
            
            for index, (next_x, next_y) in enumerate(stores):
                if visited[index]:
                    continue
                if abs(next_x-x)+abs(next_y-y)<=1000:
                    queue.append([next_x, next_y])
                    visited[index] = True
        
        if festival:
            print('happy')
        else:      
            print("sad")
        
    return 0


if __name__ == '__main__':
    main() 