#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// 1149번 RGB거리

int main() {

	int N;
	cin >> N;
	vector<vector<int>> dp(N + 1, vector<int>(3, 0));
	for (int i = 1; i <= N; i++) {
		int tmp[3];
		for (int j = 0; j < 3; j++) {
			cin >> tmp[j];
		}
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + tmp[0];
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + tmp[1];
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + tmp[2];
	}
	cout << *min_element(dp[N].begin(), dp[N].end());

	return 0;
}