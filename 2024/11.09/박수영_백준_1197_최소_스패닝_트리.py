import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_parent(parent_list, v):
    if parent_list[v] != v:
        parent_list[v] = find_parent(parent_list, parent_list[v])

    return parent_list[v]

def solution(n_vertex, n_edge, arr):
    """
    크루스칼 알고리즘
    1. 간선 비용이 낮은 순서대로 정렬
    2. 모든 간선을 확인
        - 사이클을 발생시키면 제외 >> 사이클 발생 여부를 어떻게 찾는가?
        - 발생시키지 않으면 최소 신장 트리에 포함
    """
    # 노드별 부모 노드를 저장할 배열 생성
    parent_list = [v for v in range(n_vertex+1)]

    # 간선 비용이 낮은 순서대로 정렬
    arr.sort(key=lambda x: x[-1])

    # 최소 스패닝 트리 생성
    mst_cost = 0

    # 모든 간선을 확인
    for v1, v2, w in arr:
        # v1, v2의 부모 노드 확인
        v1_p = find_parent(parent_list, v1)
        v2_p = find_parent(parent_list, v2)

        # 부모 노드가 같다 >> 사이클 발생 >> 제외
        if v1_p == v2_p:
            continue

        # 다르다 >> 사이클 X >> mst에 추가
        if v1_p < v2_p:
            parent_list[v2_p] = v1_p
        else:
            parent_list[v1_p] = v2_p

        mst_cost += w

    return mst_cost


def main():
    # 입력
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]

    # 함수 호출
    res = solution(V, E, data)

    # 결과 출력
    print(res)


if __name__ == "__main__":
    main()
