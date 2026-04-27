import java.util.*;

class Solution {
    static boolean[][] visited;
    static int[][] board;
    static int row, col;
    static int[] dx = {0, 1 , 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int answer;

    public int islandPerimeter(int[][] grid) {
        /*
        Island의 둘레 구하기
        첫 시작은 +4
        bfs로 탐색 -> 새로운 땅을 찾을 때마다 +2 (+3-1)
            다만, 새로운 땅을 추가할 때, 해당 위치에서 주변에 visited로 표시된 땅이 있는지 확인
            만약 visited된 땅이 추가로 존재한다면, 해당 위치에서는 +0 (+2-2) 이다
        */

        // 1. 초기화
        row = grid.length;
        col = grid[0].length;
        board = grid;
        visited = new boolean[row][col];
        answer = 0;

        // 2. grid 전체를 순회하면서 처음으로 1이 나타나면 bfs를 한번만 수행(Island 는 1개이므로)
        Outer: for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == 1) {
                    answer = 4;
                    bfs(i, j);
                    break Outer;
                }
            }
        }

        return answer;
    }

    public static void bfs(int curX, int curY) {
        Queue<int[]> myQueue = new ArrayDeque<>();
        visited[curX][curY] = true;
        myQueue.offer(new int[] {curX, curY});

        // 3. 큐에 있는 요소들이 사라질 때까지 탐색 (Island에 속한 요소들 방문표시)
        while (!myQueue.isEmpty()) {
            int[] curPos = myQueue.poll();

            for (int i = 0; i < 4; i++) {
                int newX = curPos[0] + dx[i];
                int newY = curPos[1] + dy[i];

                if (!checkBoundary(newX, newY)) continue;

                if (!visited[newX][newY] && board[newX][newY] == 1) {
                    // 4. 새로운 땅을 찾았을 때 현재위치를 제외하고 주위에 visited된 땅이 있는지 확인
                    if (!checkNearVisited(newX, newY)) {
                        answer += 2;
                    }

                    visited[newX][newY] = true;
                    myQueue.offer(new int[] {newX, newY});
                }
            }
        }
    }

    public static boolean checkBoundary(int x, int y) {
        if (x >= row || x < 0 || y >= col || y < 0) {
            return false;
        }
        return true;
    }

    public static boolean checkNearVisited(int x, int y) {
        int nearVisitedCnt = 0;

        for (int j = 0; j < 4; j++) {
            int nearVX = x + dx[j];
            int nearVY = y + dy[j];

            if (!checkBoundary(nearVX, nearVY)) continue;

            if (visited[nearVX][nearVY]) {
                nearVisitedCnt++;
            }
        }

        if (nearVisitedCnt == 1) {
            return false;
        }
        return true;
    }
}
