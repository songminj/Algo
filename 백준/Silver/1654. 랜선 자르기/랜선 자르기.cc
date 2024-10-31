#include <iostream>
#include <algorithm>
#include <vector>

// 1654번 랜선자르기 
using namespace std;

long long countLans(vector<long long>& lans, long long length) {
	long long count = 0;
	for (long long lan : lans) {
		count += lan / length;
	}
	return count;
}

long long search(vector<long long> &v, int N) {
	long long l = 1;
	long long r = *max_element(v.begin(), v.end());
	long long res = 0;
	while (l <= r) {
		long long mid = (l + r) / 2;
		if (countLans(v, mid) >= N) {
			res = mid;
			l = mid + 1;
		}
		else {
			r = mid - 1;
		}
	}
	return res;
}

vector<long long> lan;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int K, N;
	cin >> K >> N;
	lan.resize(K, 0);

	for (int i = 0; i < K; i++) {
		cin >> lan[i];
	}
	cout << search(lan, N);

	return 0;
}