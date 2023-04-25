#include <cstdio>
#include <vector>

using namespace std;

constexpr int MAX_N = 100000;

int answer[1 + MAX_N];
int N;
vector<int> graph[1 + MAX_N];

void dfs(int cur_node, int prev_node);

int main() {
    scanf("%d", &N);

    for (int i = 0, U, V; N > i; ++i) {
        scanf("%d%d", &U, &V);

        graph[U].emplace_back(V);
        graph[V].emplace_back(U);
    }

    dfs(1, 1);

    for (int i = 2; N >= i; ++i) {
        printf("%d\n", answer[i]);
    }

    return 0;
}

void dfs(int cur_node, int prev_node) {
    for (auto next_node : graph[cur_node]) {
        if (prev_node != next_node) {
            answer[next_node] = cur_node;
            dfs(next_node, cur_node);
        }
    }

    return;
}