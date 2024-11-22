#include <iostream>

using namespace std;

int tc;
int M, N, x, y;

// 최대공약수
int gcd(int a, int b) {
	if (a % b == 0) {
		return b;
	}
	return gcd(b, a % b);
}

// 최소공배수
int lcm(int a, int b) {
	return (a * b) / gcd(a, b);
}

void solution() {
	int result = -1;

	for (int i = x; i <= lcm(M, N); i += M) {
		int ny = i % N;
		if (ny == 0) {
			ny = N;
		}
		if (ny == y) {
			result = i;
			break;
		}
	}

	cout << result << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> tc;
	while (tc--) {
		cin >> M >> N >> x >> y;
		solution();
	}
	return 0;
}