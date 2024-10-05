#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;
// boj 2252번 줄 세우기 (위상정렬) 

int N, M;
map<int, vector<int>> students;
vector<int> indegree;

void topology() {
	queue<int> queue;
	for (int i = 1; i <= N; i++) {
		if (indegree[i] == 0) {
			queue.push(i);
		}
	}
	int x;
	while (!queue.empty()) {
		x = queue.front();
		queue.pop();
		cout << x << " ";
		for (int t : students[x]) {
			indegree[t]--;
			if (indegree[t] == 0) {
				queue.push(t);
			}
		}
	}
	return;
}

int main() {
	ios_base::sync_with_stdio(false); 
	cin.tie(0); 
	cout.tie(0);

	cin >> N >> M;
	indegree.resize(N + 1, 0);
	
	int a;
	int b;
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		students[a].push_back(b);
		indegree[b]++;
	}
	
	topology();
	return 0;
}