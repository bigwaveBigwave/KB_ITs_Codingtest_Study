#include <string>
#include <vector>

using namespace std;


vector<bool> visited;

void dfs(int node, const vector<vector<int>>& computers) {
    visited[node] = true;

    for (int i = 0; i < computers.size(); i++) {
        if (computers[node][i] == 1 && !visited[i]) {
            dfs(i, computers);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    visited.assign(n, false);
    int count = 0;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, computers);
            count++;
        }
    }

    return count;
}