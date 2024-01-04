#include <cstdio>
#include <cstring>

using namespace std;

constexpr int MAX_N = 100000;

int answer;
int T, N;
int graph[1 + MAX_N];
int color;
int visited[1 + MAX_N];
int cnt[1 + MAX_N];

void dfs(int node, int pdepth);

int main() {
    for (scanf("%d", &T); T--; ) {
        /*
         * Input.
         */
        scanf("%d", &N);

        for (int i = 1; N >= i; ++i) {
            scanf("%d", &graph[i]);
        }

        /*
         * Compute.
         */
        answer = N;

        for (int i = 1; N >= i; ++i) {
            if (!visited[i]) {
                ++color;

                dfs(i, 1);
            }
        }
        
        /*
         * Output.
         */
        printf("%d\n", answer);

        /*
         * Reset.
         */
        memset(visited, 0, sizeof(visited));
        color = 0;
    }

    return 0;
}

void dfs(int node, int pdepth) {
    cnt[node] = pdepth;
    visited[node] = color;

    if (color == visited[graph[node]]) {
        answer -= pdepth - cnt[graph[node]] + 1;
    }
    else if (!visited[graph[node]]) {
        dfs(graph[node], pdepth + 1);
    }

    return;
}