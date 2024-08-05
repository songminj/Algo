#include <iostream>
#include <algorithm>

using namespace std;

int X, Y;
int main()
{
    cin >> X >> Y;
    int cnt = 0;
    cnt = min(X, Y)/10 + X+Y;
    cout << cnt;
}