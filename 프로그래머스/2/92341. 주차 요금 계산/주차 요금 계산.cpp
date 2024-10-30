#include <string>
#include <vector>
#include <map>
#include <cmath> // std::ceil 사용을 위해 필요

using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, int> totalTime; // 각 차량의 총 주차 시간을 저장할 맵
    map<string, int> inTime; // 입차 시간을 저장할 맵

    for (string rec : records) {
        string carNumber = rec.substr(6, 4);
        int hour = stoi(rec.substr(0, 2));
        int minute = stoi(rec.substr(3, 2));
        int time = hour * 60 + minute; // 시간을 분 단위로 변환

        if (rec.substr(11, 2) == "IN") {
            inTime[carNumber] = time; // 입차 시간 기록
        } else {
            int duration = time - inTime[carNumber];
            totalTime[carNumber] += duration; // 주차 시간 누적
            inTime.erase(carNumber); // 입차 시간 삭제
        }
    }

    // 출차 기록이 없는 차량의 시간 계산 (23:59 출차 처리)
    for (auto& car : inTime) {
        totalTime[car.first] += 1439 - car.second; // 1439는 23:59의 분 단위 표현
    }

    // 각 차량에 대해 요금 계산
    for (auto& car : totalTime) {
        int time = car.second;
        int cost = fees[1]; // 기본 요금

        if (time > fees[0]) {
            cost += ceil((time - fees[0]) / (double)fees[2]) * fees[3];
        }
        answer.push_back(cost);
    }

    return answer;
}
