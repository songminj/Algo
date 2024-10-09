#include <string>
#include <vector>

using namespace std;

int check(int n) {
    int cnt = 0;
    while (n){
        if (n%2 == 1) {
            cnt++;
        }
        n /= 2;
    }
    return cnt;
}


int solution(int n) {
    int answer = n;
    int cnt_n = check(n);
    
    while (true) {
        n++;
        if (check(n) == cnt_n) {
            break;
        }
    }
    
    return n;
}