import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    
    keywords = set()
    
    for _ in range(N):
        keywords.add(sys.stdin.readline().strip())
        
    for _ in range(M):
        words = sys.stdin.readline().strip().split(",")
        for word in words:
            if word in keywords:
                keywords.remove(word)
            else:
                pass
        print(len(keywords))
        
    return 0


if __name__ == '__main__':
    main()
    