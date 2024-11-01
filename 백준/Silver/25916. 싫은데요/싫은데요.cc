#include <iostream>
#include <vector>
#include <cmath>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	int n;
	long long m;
	cin >> n >> m;

	vector<int> holes(n);
	for (int i = 0; i < n; i++) {
		cin >> holes[i];
	}
	
	long long now_sum = 0;
	int left = 0;
	long long max_v = 0;

	for (int right = 0; right < n; right++) {
		now_sum += holes[right];

		while (now_sum > m) {
			now_sum -= holes[left];
			left++;
		}

		max_v = max(max_v, now_sum);
	}
	cout << max_v;

	return 0;
}