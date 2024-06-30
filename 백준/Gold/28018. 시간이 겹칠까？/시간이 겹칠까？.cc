#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, Q;
    cin >> N;
    vector<pair<int, int>> student(N);
    for (int i = 0; i < N; i++) {
        cin >> student[i].first >> student[i].second;
    }
    
    cin >> Q;
    vector<int> time(Q);
    vector<int> record(1000002, 0);  // 0으로 초기화된 벡터 사용
    for (int i = 0; i < Q; i++) {
        cin >> time[i];
    }
    
    // 누적합 계산, 범위기반은 이렇게 변수 : 덩어리
    for (const auto& s: student){
		record[s.first]++;
		record[s.second + 1]--;
	}

    for (int i = 1; i < 1000002; i++) {
        record[i] += record[i - 1];
    }
    for (int t : time) {
        cout << record[t] << "\n";
    }
	
	return 0;
}