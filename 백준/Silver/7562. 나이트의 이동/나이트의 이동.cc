#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int TC;
int n;
int r1, r2, c1, c2;
pair<int, int> knight[] = {
{1, -2}, {1, 2},
{2, -1}, {2, 1},
{-2, -1} , {-1, 2},
{-2, 1}, {-1, -2}
};


int main() {
	ios::sync_with_stdio(0);
	cout.tie(0);
	cin.tie(0);
	
	cin >> TC;
	for (int tc = 0; tc < TC; tc++) {

		cin >> n;
		cin >> r1 >> c1 >> r2 >> c2;
		vector<vector<int>> arr(n, vector<int>(n, 0));
		vector<vector<bool>> visited(n, vector<bool>(n, false));
		
		queue<tuple<int, int, int>> queue;
		pair<int, int> node;
		queue.push({r1, c1, 0});
		visited[r1][c1] = true;

		while (!queue.empty()) {
			auto node = queue.front();
			queue.pop();

			int x = get<0>(node);  // tuple에서 값 꺼내기
			int y = get<1>(node);
			int dist = get<2>(node);

			if (x == r2 && y == c2) {
				cout << dist << "\n";
				break;
			}

			for (int i = 0; i < 8; i++) {
				int dx = x + knight[i].first;
				int dy = y + knight[i].second;

				if (0 <= dx && dx < n && 0 <= dy && dy < n && !visited[dx][dy]) {
					visited[dx][dy] = true;
					queue.push({ dx, dy, dist+1});

				}
			}
		}
	}

	return 0;
}