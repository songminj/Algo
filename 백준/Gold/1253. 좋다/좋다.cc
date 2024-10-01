#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// boj 1253번 좋다 

int N;
int l, r;
long now;
int main() {
	cin >> N;
	int goodNums = 0;
	vector<int> arr(N);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	sort(arr.begin(), arr.end());
	
	for (int i = 0; i < N; i++) {
		int target = arr[i];
		l = 0;
		r = N - 1;

		while (l < r) {
			if (l == i) {
				l += 1;
				continue;
			}
			if (r == i) {
				r -= 1;
				continue;
			}

			now = arr[l] + arr[r];
			if (now == target) {
				goodNums++;
				break;
			}
			else if (now < target) {
				l += 1;
			}
			else {
				r -= 1;
			}
		}

	}
	cout << goodNums;
	return 0;
}