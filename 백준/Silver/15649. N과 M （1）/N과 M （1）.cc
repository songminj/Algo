#include <iostream>

using namespace std;

int N, M;
int v[8];
bool visited[8];

void backTracking(int idx) {
	if (idx == M) {
		for (int i = 0; i < idx; i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
		return;
	}
	for (int i = 0; i < N; i++) {
		if (visited[i]) continue;
		visited[i] = true;
		v[idx] = i + 1;
		backTracking(idx + 1);
		visited[i] = false;
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	backTracking(0);
	return 0;
}