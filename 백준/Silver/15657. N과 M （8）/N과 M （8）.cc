#include <iostream>
#include <algorithm>

using namespace std;

// N과 M (7)
int N, M;
int v[8];
int arr[8];
bool visited[8];

void backTracking(int idx, int n) {
	if (idx == M) {
		for (int i = 0; i < M; i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = n; i < N; i++) {
		v[idx] = arr[i];
		backTracking(idx + 1, i);
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