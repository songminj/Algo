#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());
    int s = 0; int e = people.size()-1;
    while (s <= e){
        if (s == e){
            answer++;
            break;
        }
        if (people[s] + people[e] <= limit) {
            s++;
            e--;
            answer++;
        } else {
            e--;
            answer++;
        }
    }
    
    return answer;
}