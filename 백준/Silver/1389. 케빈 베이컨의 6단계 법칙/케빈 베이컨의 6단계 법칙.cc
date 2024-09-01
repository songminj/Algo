#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

vector<vector<int>> adj_d;
vector<int> val;
vector<int> visited;

void kevin_bacon(int k) {
    queue<int> q;
    q.push(k);
    visited[k] = 1;

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        for (int y : adj_d[x]) {
            if (!visited[y]) {
                visited[y] = visited[x] + 1;
                q.push(y);
            }
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    adj_d.resize(n + 1);
    val.resize(n + 1);

    // 인접 리스트 생성
    for (int i = 0; i < m; ++i) {
        int s, e;
        cin >> s >> e;
        adj_d[s].push_back(e);
        adj_d[e].push_back(s);
    }

    for (int i = 1; i <= n; ++i) {
        visited.assign(n + 1, 0);
        kevin_bacon(i);
        int sum = 0;
        for (int j = 1; j <= n; ++j) {
            sum += visited[j];
        }
        val[i] = sum;
    }

    int min_val = INT_MAX;
    int answer = 0;

    for (int i = 1; i <= n; ++i) {
        if (val[i] < min_val) {
            min_val = val[i];
            answer = i;
        }
    }

    cout << answer << endl;

    return 0;
}
