#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    int n = array.size();
    vector<int> answer;
    
    for(vector<int> cmd: commands){
        vector<int> sliced(cmd[1]-cmd[0]+1, 0);
        int idx =0;
        for (int i = cmd[0]-1; i < cmd[1]; i++){
            sliced[idx] = array[i];
            idx++;
        }
        sort(sliced.begin(), sliced.end());
        answer.push_back(sliced[cmd[2]-1]);
    }
    return answer;
}