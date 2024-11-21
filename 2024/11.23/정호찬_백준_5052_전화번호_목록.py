import sys

input = sys.stdin.readline

class Node:
    def __init__(self, data:str):
        self.data = data
        self.child = {str(idx):None for idx in range(10)} #전화번호 최대 10자리
        self.check = False #해당 노드를 마지막으로 끝나는 문자열이있으면 True

class Trie:
    def __init__(self):
        self.root = Node('')
    
    def insert(self, phone:str):
        tmp = self.root

        for i in phone:
            if tmp.child[i] is None: # 해당 자식이 비어 있다면 새로추가
                new = Node(i)
                tmp.child[i] = new
            tmp = tmp.child[i] # 다음 번호의 원소로 이동

        tmp.check = True # 단어가 끝날때 끝났음을

    def consistency(self, phone:str):
        tmp = self.root

        for i in phone: # 해당 번호를 돌면서 번호가 끝나기 전에 끝나는 단어가 있다면 False
            if tmp.check:
                return False
            tmp = tmp.child[i]

        return (True)

for _ in range(int(input())):
    n = int(input())
    phone_lst = []
    T = Trie()

    for _ in range(n):
        phone = input().strip()
        T.insert(phone)
        phone_lst.append(phone)
    
    for p in phone_lst:
        if (T.consistency(p) == False):
            print('NO')
            break
    else:
        print('YES')
