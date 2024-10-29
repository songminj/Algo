#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 9723번 Right Triangle

int T;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> T;
	for (int i = 1; i <= T; i++) {
		vector<int> lns(3);
		for (int j = 0; j < 3; j++) {
			cin >> lns[j];
		}
		sort(lns.begin(), lns.end());
		if (lns[0] * lns[0] + lns[1]*lns[1] == lns[2]*lns[2]) {
			cout << "Case #" << i << ": YES\n";
		}
		else {
			cout << "Case #" << i << ": NO\n";
		}
	}

	return 0;
}