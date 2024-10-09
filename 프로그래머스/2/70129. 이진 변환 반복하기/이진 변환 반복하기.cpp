#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer(2, 0);
    int removed = 0;
    
    while (s != "1"){
        int length = s.size();
        int cnt_one = 0;
        
        for(char c: s){
            if (c == '1') {
                cnt_one++;
            } else {
                answer[1]++;
            }
        }
        s = "";
        int num = cnt_one;
        while(num > 0){
            s = to_string(num % 2) + s;
            num /= 2;
        }
        answer[0]++;
            
    }
    
    return answer;
}