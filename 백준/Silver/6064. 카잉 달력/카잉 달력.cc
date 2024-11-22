#include <iostream>

using namespace std;

// 최대공약수
int gcd(int a, int b) {
	if  (b == 0) {
		return a;
	}
	return gcd(b, a % b);
}

// 최소공배수
int lcm(int a, int b) {
	return (a * b) / gcd(a, b);
}

int solution(int M, int N, int x, int y) {
	int max = lcm(M, N);
	for (int i = x; i <= max; i += M) {
		int ny = i % N;
		if (ny == 0) {
			ny = N;
		}
		if (ny == y) {
			return i;
		}
	}

	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int M, N, x, y, tc;;
	cin >> tc;
	while (tc--) {
		cin >> M >> N >> x >> y;
		cout << solution(M, N, x, y) << "\n";
	}
	return 0;
}