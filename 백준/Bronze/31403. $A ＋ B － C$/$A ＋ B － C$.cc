#include <iostream>
#include <string>

using namespace std;


int main() {
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;
    // 수로 생각했을 때  
    cout << a+b-c << "\n";
    
    // 문자로 생각했을 때 
    string ab = to_string(a) + to_string(b);

    cout << stoi(ab) -c << "\n";
    return 0;
}
