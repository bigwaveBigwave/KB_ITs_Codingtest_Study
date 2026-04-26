import java.util.*;

class Network {
    boolean[] visited;

    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, computers);
                answer++;
            }
        }

        return answer;
    }

    public void dfs(int node, int[][] computers) {
        visited[node] = true;

        for (int i = 0; i < computers.length; i++) {
            if (computers[node][i] == 1 && !visited[i]) {
                dfs(i, computers);
            }
        }
    }
}