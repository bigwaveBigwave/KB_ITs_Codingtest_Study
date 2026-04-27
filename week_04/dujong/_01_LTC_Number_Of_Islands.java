import java.util.*;

class Solution {
    static boolean[][] visited;
    static int[] dx = {0, 1 , 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static char[][] board;
    static int m, n;

    public int numIslands(char[][] grid) {
        // 1. 초기화
        m = grid.length;
        n = grid[0].length;
        visited = new boolean[m][n];
        board = grid;
        int answer = 0;

        // 2. gird 전체를 순회하면서 방문하지 않았고, '1'인 위치에서 bfs 수행
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && board[i][j] == '1') {
                    answer++;
                    bfs(i, j);
                }
            }
        }

        return answer;
    }

    public static void bfs(int curX, int curY) {
        Queue<int[]> myQueue = new ArrayDeque<>();
        visited[curX][curY] = true; // 3. 방문 표시는 큐에 추가할 때 수행
        myQueue.offer(new int[] {curX, curY});

        // 4. 큐에 있는 요소들이 사라질 때까지 탐색 (Island에 속한 요소들 방문표시)
        while (!myQueue.isEmpty()) {
            int[] curPos = myQueue.poll();

            for (int i = 0; i < 4; i++) {
                int newX = curPos[0] + dx[i];
                int newY = curPos[1] + dy[i];

                if (newX >= m || newX < 0 || newY >= n || newY < 0) {
                    continue;
                }

                if (!visited[newX][newY] && board[newX][newY] == '1') {
                    visited[newX][newY] = true;
                    myQueue.offer(new int[] {newX, newY});
                }
            }

        }
    }
}
