package week_03.jiwon;

public class Network {
    public int network(int n, int[][] computers) {
        int count = 0;
        boolean[] visited = new boolean[n];
        
        // 모든 컴퓨터 탐색
        for (int i = 0; i < n; i++) {
            // 아직 방문하지 않은 컴퓨터 발견하면
            if (!visited[i]) {
                count++;    // 네트워크 수 1 증가시키고
                dfs(i, n, computers, visited);  // dfs 진행
            }
        }
        
        return count;
    }
    
    void dfs(int cur, int n, int[][] computers, boolean[] visited) {
        // 현재 컴퓨터 방문 처리
        visited[cur] = true;
        
        for (int next = 0; next < n; next++) {
            // 1) 현재와 다음 컴퓨터 연결되어 있고, 2) 다음 컴퓨터 방문하지 않은 경우
            // -> dfs 진행 
            if(computers[cur][next] == 1 && !visited[next]) {
                dfs(next, n, computers, visited);
            }
        }
    }

    public static void main(String[] args) {
        Network n = new Network();

        int size = 3;
        int[][] computers = {
            {1, 1, 0},
            {1, 1, 1},
            {0, 1, 1}
        };
        
        System.out.println("Network Count: " + n.network(size, computers)); // 예상 결과: 2

    }
}
