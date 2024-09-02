#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

string str1, str2;
int ans = 0;

int main() {
	vector<int> v1(26, 0);
	vector<int> v2(26, 0);
	cin >> str1 >> str2;

	for (auto s : str1) {
		int a = s - 'a';
		v1[a]++;
	}
	for (auto s : str2) {
		int a = s - 'a';
		v2[a]++;
	}
	for (int i = 0; i < 26; i++) {
		ans += abs(v1[i] - v2[i]);
	}
	cout << ans;
	return 0;
}