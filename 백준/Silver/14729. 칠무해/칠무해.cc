#include <iostream>
#include <map>
#include <iomanip>

using namespace std;

int main() {
	int N;
	float m;
	cin >> N;

	map<float, int> stds;

	for (int i = 0; i < N; i++) {
		cin >> m;
		// stds에 있는 key이면 value를 +1해주고 없으면 1을 해준다
		stds[m]++;
	}

	int printCnt = 0;
	for (const auto& pair : stds) {
		for (int j = 0; j < pair.second; j++) {
			cout << fixed << setprecision(3) << pair.first << "\n";
			printCnt++;
			if (printCnt == 7) {
				break;
			}
		}
		if (printCnt == 7) {
			break;
		}
	}

	return 0;
}