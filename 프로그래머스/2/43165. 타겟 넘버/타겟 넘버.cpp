#include <vector>

using namespace std;

int dfs(const vector<int>& numbers, int target, int idx, int currentSum) {
    if (idx == numbers.size()) {
        return (currentSum == target) ? 1 : 0;
    }
    
    // 현재 숫자를 더하거나 빼는 두 가지 경우
    return dfs(numbers, target, idx + 1, currentSum + numbers[idx]) +
           dfs(numbers, target, idx + 1, currentSum - numbers[idx]);
}

int solution(vector<int> numbers, int target) {
    return dfs(numbers, target, 0, 0); // 시작은 인덱스 0, 합계 0에서 시작
}
