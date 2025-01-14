#include <iostream>

using namespace std;

const int MOD = 1000000000;
int n;

int main() {
    cin >> n;
    
    int abs_n = abs(n);

    long long dp[1000001];
    dp[0] = 0;
    dp[1] = 1; 

    for (int i = 2; i <= abs_n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }

    if (n > 0) {
        cout << 1 << "\n";
    }
    else if (n == 0) {
        cout << 0 << "\n";
    }
    else {
        cout << ((n % 2 == 0) ? -1 : 1) << "\n";
    }
    cout << dp[abs_n] << "\n";

    return 0;
}
