#include <string>
#include <vector>

using namespace std;

bool visited[200];

int Dfs(int n, vector<vector<int>>& computers, int v){
    for (int i =0; i < n; i++){
        if (i != n && !visited[i] && computers[v][i]){
            visited[i] = true;
            Dfs(n, computers, i);
        }
    }
    return 0;
}

int solution(int n, vector<vector<int>> computers) {
    int ans = 0;
    for (int i = 0; i < n; i++){
        if (!visited[i]){
            visited[i] = true;
            Dfs(n, computers, i);
            ans++;
        }
    }

    return ans;
}