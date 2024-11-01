#include <iostream>
#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

// 13305번 주유소 

int N;
int road[100001];
int cost[100001];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	
	// 값 저장
	for (int i = 0; i < N-1; i++) {
		cin >> road[i];
	}
	for (int i = 0; i < N; i++) {
		cin >> cost[i];
	}
	long long ans = 0;
	int min_v = INT_MAX;

	for (int i = 0; i < N; i++) {
		if (min_v > cost[i]) {
			min_v = cost[i];
		}
		ans += (min_v * road[i]);
	}
	
	cout << ans;

	return 0;
}