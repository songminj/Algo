#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

long long binary(long long s, long long e, vector<int>& T, int N, int M) {
    while (s <= e) {
        long long mid = s + (e - s) / 2;
        long long checked = 0;
        for (int i = 0; i < N; i++) {
            checked += mid / T[i];
            if (checked >= M) break;  
        }
        if (checked >= M)
            e = mid - 1;
        else
            s = mid + 1;
    }
    return s;
}

int main() {
    int N, M;
    cin >> N >> M;
    // 런타임 변수로 배열을 만들려면 vector을 사용해야함.
    vector<int> T(N);
    for (int i = 0; i < N; i++) {
        cin >> T[i];
    }
    long long max_val = *max_element(T.begin(), T.end());
    cout << binary(0, max_val * (long long)M, T, N, M);
    return 0;
}