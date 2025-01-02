#include <iostream>
#include <list>
#include <vector>

using namespace std;

int P;

int main() {
    cin >> P; // 테스트 케이스 수
    for (int tc = 1; tc <= P; tc++) {
        int testCaseNumber, moves = 0;
        cin >> testCaseNumber;

        list<int> line; // 현재 줄을 나타내는 linked list
        vector<int> heights(20); // 키 정보
        for (int i = 0; i < 20; i++) {
            cin >> heights[i];
        }

        for (int height : heights) {
            // 자신이 설 위치를 찾는다
            auto it = line.begin();
            int stepsBack = 0; // 뒤로 물러나는 횟수

            while (it != line.end() && *it < height) {
                ++it;
                ++stepsBack; // 한 칸 뒤로 이동
            }

            // 학생을 해당 위치에 삽입
            line.insert(it, height);

            // 총 물러난 횟수에 추가
            moves += distance(it, line.end());
        }

        // 결과 출력
        cout << testCaseNumber << " " << moves << endl;
    }

    return 0;
}
