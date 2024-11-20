"""
접두어 판별
"""
def solution(n, numbers):
    """
    - startswith 사용
    - python3 시간 초과
    - pypy3 통과(메모리116548KB_시간4360ms)
    """
    numbers.sort(key=lambda x: len(x))

    for i in range(n):
        for j in range(i+1, n):
            if numbers[j].startswith(numbers[i]):
                return "NO"

    return "YES"

def solution2(n, numbers):
    """
    해쉬맵 사용
    - python3 통과(메모리32344KB_시간4988ms)
    - pypy3 통과(메모리126792KB_시간276ms)
    """
    hashmap = {}
    for number in numbers:
        hashmap[number] = True

    for number in numbers:
        tmp = str()
        for digit in number:
            tmp += digit
            try:
                if hashmap[tmp] and tmp != number:
                    return "NO"
            except KeyError:
                pass

    return "YES"

def solution3():
    """
    Trie 알고리즘
    - python3 시간 초과
    - pypy3 통과(메모리220056KB_시간848ms)
    """
    class Node:
        def __init__(self, data):
            self.data = data
            self.child = [None for _ in range(10)]
            self.check = False

    class Trie:
        def __init__(self, ):
            self.root = Node('')

        def insert(self, number):
            parent = self.root
            for digit in number:
                if parent.child[digit] == None:
                    new_child = Node(digit)
                    parent.child[digit] = new_child
                    parent = new_child
                else:
                    parent = parent.child[digit]

            parent.check = True

        def startswith(self, number):
            parent = self.root
            for digit in number:
                if parent.check:
                    return True
                
                parent = parent.child[digit]
            
            return False

    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [list(map(int, input())) for _ in range(n)]
        trie = Trie()

        for number in numbers:
            trie.insert(number)
        
        # 일관성 확인
        is_consistent = True
        for number in numbers:
            if trie.startswith(number):
                is_consistent = False
                break

        if is_consistent: print("YES")
        else: print("NO")
                

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [input() for _ in range(n)]

        res = solution2(n, numbers)

        print(res)


if __name__ == "__main__":
    main()
    # solution3()
