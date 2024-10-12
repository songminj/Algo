#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

vector<int> graph[1001]; // 인접 리스트
bool visited[1001];      // 방문 여부 확인 배열

// DFS 함수
void dfs(int v) {
    visited[v] = true;
    cout << v << " ";

    for (int i = 0; i < graph[v].size(); i++) {
        int next = graph[v][i];
        if (!visited[next]) {
            dfs(next);
        }
    }
}

// BFS 함수
void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int v = q.front();
        q.pop();
        cout << v << " ";

        for (int i = 0; i < graph[v].size(); i++) {
            int next = graph[v][i];
            if (!visited[next]) {
                q.push(next);
                visited[next] = true;
            }
        }
    }
}

int main() {
    int n, m, v; // n: 정점의 개수, m: 간선의 개수, v: 시작 정점
    cin >> n >> m >> v;

    // 간선 입력
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a); 
    }

    // 정점 번호가 작은 것부터 방문하기 위해 인접 리스트 정렬
    for (int i = 1; i <= n; i++) {
        sort(graph[i].begin(), graph[i].end());
        for (int j = 0; j < graph[i].size(); j++) {
        }
    }

    dfs(v);
    cout << endl;

    // BFS 수행을 위해 visited 배열 초기화
    fill(visited, visited + 1001, false);

    bfs(v);
    cout << endl;

    return 0;
}
