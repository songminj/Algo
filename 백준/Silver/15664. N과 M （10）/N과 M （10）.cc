#include <iostream>
#include <algorithm>

using namespace std;

// N과 M (10)
int N, M;
int v[8];
int arr[8];
bool visited[8] = { false };

void backTracking(int idx, int n) {
	if (idx == M) {
		for (int i = 0; i < M; i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
		return;
	}
	int temp = 0;

	for (int i = n; i < N; i++) {
		if (!visited[i] && arr[i] != temp) {
			v[idx] = arr[i];
			temp = v[idx];
			visited[i] = true;
			backTracking(idx + 1, i);
			visited[i] = false;
		}
	}
}


int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(0);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	sort(arr, arr+N);

	backTracking(0, 0);
	return 0;
}