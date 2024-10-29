#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

// 1339번 단어수학 

// 내림차순 
bool cmp(int& a, int& b) {
	return a > b;
}

int N;
int arr[26];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;

	// 알파벳이 몇번째 자릿수에 해당하는지 
	for (int i = 0; i < N; i++) {

		string word;
		cin >> word;
		int pow = 1;
		for (int j = word.length() - 1; j >= 0; j--) {
			arr[word[j] - 'A'] += pow;
			pow *= 10;
		}
	}
	sort(arr, arr + 26, cmp);

	int num = 9;
	int ans = 0;
	for (int i = 0; i < 26; i++) {
		if (arr[i] == 0) 
			break;
		ans += arr[i] * num;
		num--;
	}

	cout << ans;

	return 0;
}