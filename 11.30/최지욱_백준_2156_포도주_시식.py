def main():
    N= int(input())
    wine = []
    
    for _ in range(N):
        wine.append(int(input()))
    
    if N<3:
        print(sum(wine))
        return 0
    
    case1 = wine[0] + wine[1]   ## OO -> (OOX)
    case2 = wine[0]             ## OX -> (OXO, OXX)
    case3 = wine[1]             ## XO -> (XOO, XOX)
    case4 = 0                   ## XX -> (XXO, XXX)
      
    for glass in wine[2:]:
        case1, case2, case3, case4 = case3+glass, max(case1,case3), max(case2+glass, case4+glass), max(case2, case4)
        
    print(max(case1, case2, case3, case4))

main()