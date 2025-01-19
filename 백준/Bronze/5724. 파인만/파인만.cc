#include <iostream>

using namespace std;

// # 5724 파인만
int n;
int dp[101];

int main() {
    for (int i = 1; i <= 100; i++) {
        dp[i] = i * i;
    }
    while (true) {
        cin >> n;
        int res = 0;
        if (n == 0) {
            break;
        }
        for (int i = 1; i <= n; i++) {
            res += dp[i];
        }
        cout << res << "\n";
    }
    return 0;
}