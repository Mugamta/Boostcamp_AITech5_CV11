"""
구현
- doubly linked list로 푸는 문제
"""
def solution(n, k, cmd):
    # 표 생성
    table = ['O'] * n
    table_info = {i:[i-1, i+1] for i in range(n)}
    
    # head, tail 처리
    table_info[0][0] = None
    table_info[n-1][1] = None
    
    # 삭제된 행 정보 기록
    delete = []
    
    # 명령 수행
    for c in cmd:
        # 위
        if c[0] == 'U':
            _, offset = c.split()
            for _ in range(int(offset)):
                front, _ = table_info[k]
                k = front
        
        # 아래
        elif c[0] == 'D':
            _, offset = c.split()
            for _ in range(int(offset)):
                _, rear = table_info[k]
                k = rear
        
        # 삭제
        elif c[0] == 'C':
            front, rear = table_info[k]
            
            table[k] = 'X'
            delete.append([front, k, rear])
            
            # 삭제한 행이 head인 경우
            if front == None:
                k = rear # 바로 뒷 행을 선택
            
            # 삭제한 행이 tail인 경우
            if rear == None:
                k = front # 바로 앞 행을 선택
            else:
                k = rear
                
            # 삭제한 행의 앞 행과 뒷 행을 연결
            if front == None:
                table_info[rear][0] = None
            elif rear == None:
                table_info[front][1] = None
            else:
                table_info[front][1] = rear
                table_info[rear][0] = front
        
        # 복구
        elif c[0] == 'Z':
            # 가장 최근에 삭제한 행 정보 불러옴 >> *가장 최근*이라는 조건이 있기 때문에, O(1)으로 복구 가능함
            front, cur, rear = delete.pop()
            
            table[cur] = 'O' # 복원
            if front == None:
                table_info[rear][0] = cur
            elif rear == None:
                table_info[front][1] = cur
            else:
                table_info[front][1] = cur
                table_info[rear][0] = cur
            
    # 출력
    return ''.join(table)        