#include <iostream>

using namespace std;

// N과 M (4)
int N, M;
int v[8];

void backTracking(int idx, int n) {
	if (idx == M) {
		for (int i = 0; i < M; i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = n; i <= N; i++) {
		v[idx] = i;
		backTracking(idx + 1, i);
	}

}


int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(0);
	cin >> N >> M;
	backTracking(0, 1);
	return 0;
}