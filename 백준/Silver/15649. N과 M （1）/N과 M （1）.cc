#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<int> v;
vector<bool> visited;

void backTracking(int depth) {
	if (depth == M) {
		for (int i = 0; i < M; i++) {
			cout << v[i] << " ";
		}
		cout << endl;
		return;
	}
	for (int i = 1; i <= N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			v.push_back(i);
			backTracking(depth+1);
			v.pop_back();
			visited[i] = false;
		}

	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	visited.resize(N + 1, false);
	backTracking(0);
	return 0;
}