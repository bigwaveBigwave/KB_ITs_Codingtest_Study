package week_07.junyeon;

public class 피로도 {
    int answer = 0;
    public int solution(int k, int[][] dungeons) {

        boolean[] visited = new boolean[dungeons.length];
        dfs(k, dungeons, visited);

        return answer;
    }

    public void dfs(int k , int[][] dungeons, boolean[] visited) {
        int check = 0;
        for (int i = 0; i < dungeons.length ; i++) {
            if (visited[i] == true) {
                check += 1;
            }
        }
        answer = (answer > check ? answer : check);
        for (int i = 0; i < dungeons.length ; i++) {
            if (visited[i] == true) continue;
            if (dungeons[i][0] <= k){
                visited[i] = true;
                dfs(k-dungeons[i][1], dungeons, visited);
                visited[i] = false;
            }

        }
    }
}
