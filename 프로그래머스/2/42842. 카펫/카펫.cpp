#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    answer.resize(2, 0);
    int x = (brown+4) / 2;
    int y = 0;
    while (x >= y) {
        if ((x -2) * (y-2) == yellow) {
            answer[0] = x;
            answer[1] = y;
            break;
        } else {
            x--;
            y++;
        }
    }
    return answer;
}