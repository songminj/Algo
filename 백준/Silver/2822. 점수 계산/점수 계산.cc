#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<pair<int, int>> scores; // (점수, 문제 번호)

    for (int i = 1; i <= 8; i++) {
        int score;
        cin >> score;
        scores.push_back({ score, i });
    }

    sort(scores.rbegin(), scores.rend());

    int total = 0;
    vector<int> numbers;

    for (int i = 0; i < 5; i++) {
        total += scores[i].first;
        numbers.push_back(scores[i].second);
    }

    sort(numbers.begin(), numbers.end());

    cout << total << endl;
    for (int i = 0; i < numbers.size(); i++) {
        cout << numbers[i] << (i == numbers.size() - 1 ? "\n" : " ");
    }

    return 0;
}
