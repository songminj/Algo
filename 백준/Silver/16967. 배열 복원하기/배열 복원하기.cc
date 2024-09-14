#include <iostream>
#include <vector>

using namespace std;

int H, W, X, Y;
int main() {
	cin >> H >> W>> X>> Y;
	vector<vector<int>> arr(X+H, vector<int>(Y+W,0));
	for (int i = 0; i < X+H; i++) {
		for (int j = 0; j < Y+W; j++) {
			cin >> arr[i][j];
		}
	}

	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			if (i >= X && j >= Y) {
				arr[i][j] -= arr[i - X][j - Y];
			} 
		}
	}

	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			cout << arr[i][j] << " ";
		}
		cout << "\n";
	}	

	return 0;
}