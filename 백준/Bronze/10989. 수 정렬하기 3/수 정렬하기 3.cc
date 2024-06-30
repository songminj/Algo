#include <iostream>
#include <vector>

using namespace std;


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int N;
	cin >> N;

	vector<int> v(10001, 0);

	for(int i = 0; i < N; i++) {
		int idx;
		cin >> idx;
		v[idx]++;
	}
	
	for (int i = 1; i < 10001; i++) {
		for (int j = 0; j < v[i]; j++) {
			cout << i <<"\n";
		}
	}
	
	return 0;
}