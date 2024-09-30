#include <iostream>

using namespace std;

int N, A, B;

int main() {
	cin >> N >> A >> B;
	int good = 1;
	int bad = 1;

	for (int i = 0; i < N; i++) {
		good += A;
		bad += B;
		if (bad > good) {
			int tmp = bad;
			bad = good;
			good = tmp;
		}
		else if (bad == good) {
			bad--;
		}

	}
	cout << good << " " << bad;

	return 0;
}