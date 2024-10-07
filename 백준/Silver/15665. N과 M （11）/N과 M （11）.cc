#include <iostream>
#include <algorithm>

using namespace std;

// N과 M (11)
int N, M;
int v[7];
int arr[7];
bool visited[7] = { false };

void backTracking(int idx) {
	if (idx == M) {
		for (int i = 0; i < M; i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
		return;
	}
	int temp = 0;

	for (int i = 0; i < N; i++) {
		if (arr[i] != temp) {
			v[idx] = arr[i];
			temp = v[idx];
			backTracking(idx + 1);
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

	backTracking(0);
	return 0;
}