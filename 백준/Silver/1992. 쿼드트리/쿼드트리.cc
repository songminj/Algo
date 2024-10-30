#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

// 1992번 쿼드트리
string arr[64];

void quadTree(int n, int y, int x) {
	char now = arr[y][x];
	
	for (int i = y; i < y + n; i++) {
		for (int j = x; j < x + n; j++) {
			if (arr[i][j] != now) {
				cout << '(';
				quadTree(n / 2, y, x);
				quadTree(n / 2, y, x + n / 2);
				quadTree(n / 2, y + n / 2, x);
				quadTree(n / 2, y + n / 2, x + n / 2);
				cout << ')';
				return;
			}
			
		}
	}
	cout << now;
	
}

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	
	quadTree(N, 0, 0);

	return 0;
}