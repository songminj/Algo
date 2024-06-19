#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N = 0;
    int A = 0, B = 0;
    int X = 0, Y = 0;

    cin >> N >> A >> B;

    int left = 8 - N;
    // 남은 학기의 전공과목개수, 비전공과목개수
    for (int i = 0; i < left; i++) {
        int x, y;
        cin >> x >> y;
        A += x * 3;
        B += min((x + y), 6) * 3;
    }

    if ((B >= 130) && (A + X * 3 >= 66)) {
        cout << "Nice";
    }
    else {
        cout << "Nae ga wae";
    }
    return 0;

}