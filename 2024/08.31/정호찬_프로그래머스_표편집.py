"""
- 풀이
연결리스트를 활용한 풀이
삭제 삽입과 같은 문제에서는 배열보다는 연결리스트가 더 빠름 
그러나 탐색에서는 느린 문제가 있음 (인덱싱)으로 접근이 불가능하기 때문에
하지만 해당 문제의 경우 현재 선택된 행을 기준으로 움직이기 때문에 선형적으로 행을 탐색하지 않아도 되기 때문에
연결리스트가 빠르다는 판단

- 정확성 평가
시  간 : 9.35ms
메모리 : 10.5MB

- 효율성 평가
시  간 : 942.04ms
메모리 : 235MB
"""

def solution(n, k, cmd):
    # 현재 행의 이전과 다음 행을 추적하는 배열
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    linked_list[0][0] = None
    linked_list[n-1][1] = None
    
    # 현재 선택된 행
    current = k
    
    # 삭제된 행을 저장하는 스택
    stack = []
    
    # 삭제된 행을 표시하는 집합
    deleted = set()

    for c in cmd:
        if c.startswith('D'):
            X = int(c.split()[1])
            for _ in range(X):
                current = linked_list[current][1]
        elif c.startswith('U'):
            X = int(c.split()[1])
            for _ in range(X):
                current = linked_list[current][0]
        elif c == 'C':
            prev, next = linked_list[current]
            stack.append((prev, current, next))
            deleted.add(current)
            
            #마지막 행이라면 현재를 이전행으로
            if next is None:
                current = prev
            else: # 아니면 다음 행으로 
                current = next
                
            # 첫번째 행이거나 마지막 행이 아니라면 삭제하고 연결
            if prev is not None:
                linked_list[prev][1] = next
            if next is not None:
                linked_list[next][0] = prev
                
        elif c == 'Z': #되돌리기 
            if stack: # 삭제된 값이 있다면 
                prev, restored, next = stack.pop() #최근 삭제 가져오기
                deleted.remove(restored) #삭제 정보 제거
                
                if prev is not None: #이전이 첫번째 행이 아니라면 이전의 다음을 restored로 되돌림
                    linked_list[prev][1] = restored
                if next is not None: #다음이 마지막 행이 아니라면 다음의 이전을 restored로 되돌림
                    linked_list[next][0] = restored
    # 삭제 정보에 있다면 X 아니면 O으로 출력
    return ''.join('O' if i not in deleted else 'X' for i in range(n))
