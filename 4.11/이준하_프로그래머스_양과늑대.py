# 10:30 시작
# 10:57 풀이 생각 (모두 탐색 해 보되, 늑대가 더 많아지는 순간에 되돌아가도록 알고리즘 구성)
# 12:14 제출

# 0은 양, 1은 늑대로 하여 edge 순회
# edge는 항상 하나의 이진트리 형태로 주어짐
def solution(info, edges):
    visited = [0] * len(info)
    global answer
    answer = 1
    # 양의 수가 늑대의 수와 같아지면 중단
    # 아니면, 탐색시의 양의 수가 커질 때 마다 answer 갱신
    # 모든 노드를 탐색하면 중단
    def dfs(s_num,w_num):
        global answer
        if s_num > w_num:
            if answer < s_num:
                answer = s_num
        else:
            return
        for p, c in edges:
            # 부모노드는 방문하고, 자식노드가 처음이면, 자식노드 방문처리
            if visited[p] and not visited[c]:
                visited[c] = 1
                # 자식노드가 양일 경우 양을 하나 추가하고, 늑대일 경우 늑대를 추가
                if info[c] == 0:
                    dfs(s_num+1, w_num)
                else:
                    dfs(s_num, w_num+1)
                # 늑대와 양의 수가 같아지는 경우, 해당 노드를 방문하지 않고 형제노드를 탐색
                visited[c] = 0
    visited[0] = 1
    dfs(1,0)
    
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))