#include <iostream>


using namespace std;


int main() {
    int N;
    int arr[6];
    int T, P;
    int resT = 0;
    int resP = 0, resP2 = 0;

    cin >> N;
    for (int i = 0; i < 6; i++) {
        cin >> arr[i];
    }
    cin >> T >> P;

    // T셔츠 묶음 개수 
    for (int i = 0; i < 6; i++) {
        if (arr[i] > 0) {
            resT += (arr[i] / T);
            if (arr[i] % T != 0) {
                resT += 1;
            }
        }
    }

    cout << resT << "\n";
    cout << N / P << " " << N % P << "\n";
    return 0;
}
