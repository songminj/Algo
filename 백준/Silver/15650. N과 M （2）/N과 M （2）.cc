#include <iostream>

using namespace std;


int N, M;
int v[8];
bool visited[8];

void backTracking(int n, int idx) {
	if (idx == M) {
		for (int i = 0; i < M; i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
		return;
	}
	for (int i = n; i <= N; ++i) {
		if (!visited[i]) {
			visited[i] = true;
			v[idx] = i;
			backTracking(i + 1, idx + 1);
			visited[i] = false;
		}
	}
}


int main() {
	cin >> N >> M;
	backTracking(1, 0);
	return 0;
}