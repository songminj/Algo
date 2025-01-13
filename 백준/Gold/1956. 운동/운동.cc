#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int INF = 100000000;
int V, E;

int main() {
    cin >> V >> E;
    
    vector<vector<int>> dist;
    dist.resize(V + 1, vector<int>(V + 1, INF));

    for (int i = 0; i < E; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        dist[a][b] = c;
    }

    for (int k = 1; k <= V; k++) {
        for (int i = 1; i <= V; i++) {
            for (int j = 1; j <= V; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    int ans = INF;

    for (int i = 1; i <= V; i++) {
        for (int j = 1; j <= V; j++) {
            if (i != j) {
                if (dist[i][j] < INF && dist[j][i] < INF) {
                    ans = min(ans, dist[i][j] + dist[j][i]);
                }
            }
        }
    }

    if (ans != INF) {
        cout << ans;
    }
    else {
        cout << -1;
    }
    return 0;
}
