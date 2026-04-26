class Solution {
    boolean[] visited;

    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, n, computers);
                answer++;
            }
        }
        return answer;
    }
    public void dfs(int i, int n, int[][] computers) {
        visited[i] = true;

        for (int j = 0; j < n; j++) {
            if (computers[i][j] == 1 && !visited[j]) {
                dfs(j, n, computers);
            }
        }
    }
}