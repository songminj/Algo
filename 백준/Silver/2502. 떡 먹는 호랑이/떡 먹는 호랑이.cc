#include <iostream>
#include <vector>

using namespace std;

pair<int, int> horang(int a, int b, int t) {
	for (int x = 1; x <= t / a; x++) {
		if ((t - a * x) % b == 0) {
			int y = (t - a * x) / b;
			if (y > 0) {
				return { x, y };
			}
		}
	}
	return { -1, -1 };
}

int main() {
	int D, K;
	cin >> D >> K;
	vector<vector<int>> v(D, vector<int>(2, 0));
	v[0][0] = 1;
	v[1][1] = 1;
	for (int i = 2; i < D; i++) {
		v[i][0] = v[i - 1][0] + v[i - 2][0];
		v[i][1] = v[i - 1][1] + v[i - 2][1];
	}

	pair<int, int> result = horang(v[D - 1][0], v[D - 1][1], K);
	cout << result.first << "\n";
	cout << result.second;

	return 0;
}