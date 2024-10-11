#include <string>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int solution(vector<int> elements) {
    set<int> s;
    int n = elements.size();
    
    for (int l = 1; l <= n; l++){
        for (int start = 0; start < n; start++){
            int sum = 0;
            for (int i = 0; i < l; i++){
                sum += elements[(start+i)%n];
            }
            s.insert(sum);
        }
    }
    
    
    return s.size();
}