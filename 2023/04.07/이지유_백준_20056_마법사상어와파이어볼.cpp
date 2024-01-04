#include <cstdio>
#include <tuple>
#include <queue>

using namespace std;

constexpr int MAX_N = 50;
constexpr int dd[2][4] = { {1, 3, 5, 7}, {0, 2, 4, 6} };

int dr[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dc[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };

struct Square {
	int cnt;
	int m_sum;
	int s_sum;
	bool d_odds;
	bool d_evens;
} map[MAX_N][MAX_N];

int answer;
int K, N, M;
queue<tuple<int,int,int,int,int>> q;

int main() {
	/*
	 * Input.
	 */
	scanf("%d%d%d", &N, &M, &K);

	dr[7] = dr[1] = dr[0] = N - 1;
	dc[7] = dc[6] = dc[5] = N - 1;

	for (int r, c, m, s, d; M--; ) {
		scanf("%d%d%d%d%d", &r, &c, &m, &s, &d);

		q.emplace(r - 1, c - 1, m, s, d);
	}

	/*
	 * Compute.
	 */
	for (int r, c, m, s, d; K--; ) {
		// Step 1.
		for (int k = 0, endk = q.size(); endk > k; ++k) {
			r = get<0>(q.front());
			c = get<1>(q.front());
			m = get<2>(q.front());
			s = get<3>(q.front());
			d = get<4>(q.front());

			q.pop();

			// Move fireball.
			r = (r + dr[d] * s) % N;
			c = (c + dc[d] * s) % N;

			if (0 == map[r][c].cnt) {
				q.emplace(r, c, 0, 0, d);
			}

			// Record onto square.
			map[r][c].cnt += 1;
			map[r][c].m_sum += m;
			map[r][c].s_sum += s;
			if (d & 1) {
				map[r][c].d_odds = true;
			}
			else {
				map[r][c].d_evens = true;
			}
		}

		// Step 2.
		for (int k = 0, endk = q.size(); endk > k; ++k) {
			r = get<0>(q.front());
			c = get<1>(q.front());
			m = map[r][c].m_sum;
			s = map[r][c].s_sum;
			d = get<4>(q.front());

			q.pop();

			// Merge fireballs.
			if (1 == map[r][c].cnt) {
				q.emplace(r, c, m, s, d);
			}
			else {
				if (m /= 5) {
					s /= map[r][c].cnt;

					for (int z = 0, idx = map[r][c].d_odds ^ map[r][c].d_evens; 4 > z; ++z) {
						q.emplace(r, c, m, s, dd[idx][z]);
					}
				}
			}

			// Reset square.
			map[r][c].cnt = 0;
			map[r][c].m_sum = 0;
			map[r][c].s_sum = 0;
			map[r][c].d_odds = false;
			map[r][c].d_evens = false;
		}
	}

	/*
	 * Output.
	 */
	for (; !q.empty(); q.pop()) {
		answer += get<2>(q.front());
	}

	printf("%d", answer);

	return 0;
}