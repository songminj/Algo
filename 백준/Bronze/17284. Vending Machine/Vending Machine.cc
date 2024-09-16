#include <iostream>
#include <vector>

using namespace std;

int res = 5000;
int n;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> v(4, 0);

    while (cin >> n) {  
        if (n >= 1 && n <= 3) {
            v[n] += 1;
        }
    }

    cout << 5000 - v[1] * 500 - v[2] * 800 - v[3] * 1000;
    return 0;
}
