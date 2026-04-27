import java.util.*;

class Solution {

    static int count;   // 섬 개수
    static boolean[][] visited; // 방문 배열

    // 방향 탐색 (상하좌우)
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    public int numIslands(char[][] grid) {

        int n = grid.length;    // 세로
        int m = grid[0].length; // 가로


        // 초기화
        count = 0;
        visited = new boolean[n][m];

        // 그리드 탐색
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                // 1) 땅 2) 방문x -> 개수 1 증가 후 bfs 
                if(!visited[i][j] && grid[i][j] == '1') {
                    count++;
                    bfs(i, j, n, m, grid);
                }
            }
        }

        return count;
    }

    void bfs(int start_y, int start_x, int n, int m, char[][] grid) {
        Queue<int[]> q = new ArrayDeque<>();

        // 시작 좌표
        q.offer(new int[]{start_y, start_x});
        visited[start_y][start_x] = true;

        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int y = cur[0];
            int x = cur[1];

            // 4방향 탐색
            for(int i=0; i<4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                
                // grid 범위 벗어나지 않는지 확인 
                if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                
                // 1) 땅 2) 방문x -> 방문처리 후 큐에 추가 
                if(grid[ny][nx] == '1' && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    q.offer(new int[]{ny, nx});
                }
            }
        }

        return;
    }
}