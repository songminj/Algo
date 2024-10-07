#include <iostream>
#include <algorithm>
#include<vector>
using namespace std;

int solution(vector<int> A, vector<int> B)
{
    int answer = 0;
    sort(A.begin(), A.end());
    sort(B.begin(), B.end(), greater<int>());
    int N = B.size();
    for (int i = 0; i < N; i++) {
        answer += (A[i]*B[i]);
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << answer;

    return answer;
}