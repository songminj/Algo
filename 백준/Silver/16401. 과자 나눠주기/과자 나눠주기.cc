#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 16401번 과자 나눠주기 

int M, N;
vector<int> snack;

bool canDo(int s) {
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		cnt += snack[i] / s;
	}
	return cnt >= M;
}

int giveSnack() {
	int left = 1;
	int right = snack[N-1] ;
	int result = 0;
	while (left <= right) {
		int mid = (left + right) / 2;
		if (canDo(mid)) {
			result = mid;
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}
	return result;

}

int main() {
	cin >> M >> N;
	snack.resize(N, 0);

	for (int i = 0; i < N; i++) {
		cin >> snack[i];
	}
	sort(snack.begin(), snack.end());
	cout << giveSnack();
	return 0;
}