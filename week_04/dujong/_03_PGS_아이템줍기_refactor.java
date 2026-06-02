import java.util.*;

class Solution {
    static int[][][] board;
    static int[][] rectangle;
    static boolean[][] visited;
    static int answer;

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        // 1. 초기화
        Solution.rectangle = rectangle;
        board = new int[51][51][5];
        visited = new boolean[51][51];
        answer = 0;

        // 2. 각 직사각형의 테두리에 있는 모든 점들을 순회하면서 유효한 위치와 방향 저장
        for (int i = 0; i < rectangle.length; i++) {
            setValidCoordinates(rectangle[i], i);
        }

        // 3. bfs를 이용해서 board를 순회
        bfs(characterX, characterY, itemX, itemY);
        return answer;
    }

    public static void bfs(int startX, int startY, int targetX, int targetY) {
        int[] dx = {1, 0, -1, 0};  // 우, 하, 좌, 상
        int[] dy = {0, -1, 0, 1};

        Queue<int[]> queue = new ArrayDeque<>();
        visited[startX][startY] = true;
        queue.offer(new int[]{startX, startY, 0});

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int curX = cur[0], curY = cur[1], depth = cur[2];

            if (curX == targetX && curY == targetY) {
                answer = depth;
                return;
            }

            for (int d = 1; d <= 4; d++) {
                if (board[curX][curY][d] == 0) continue;

                int nx = curX + dx[d - 1];
                int ny = curY + dy[d - 1];

                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny, depth + 1});
                }
            }
        }
    }

    public static void setValidCoordinates(int[] rectPos, int curIndex) {
        int x1 = rectPos[0];
        int y1 = rectPos[1];
        int x2 = rectPos[2];
        int y2 = rectPos[3];

        // 2-1. 꼭짓점 위치 유효성 및 방향 유효성 설정
        setCorner(x1, y1, curIndex, 1, 4); // 좌하단: 우, 상
        setCorner(x2, y1, curIndex, 3, 4); // 우하단: 좌, 상
        setCorner(x1, y2, curIndex, 1, 2); // 좌상단: 우, 하
        setCorner(x2, y2, curIndex, 3, 2); // 우상단: 좌, 하

        // 2-2. 위/아래 가로 변 처리 (꼭짓점 제외)
        for (int x = x1 + 1; x < x2; x++) {
            setEdge(x, y1, curIndex, 1, 3); // 아래쪽 변: 우, 좌
            setEdge(x, y2, curIndex, 1, 3); // 위쪽 변: 우, 좌
        }

        // 2-3. 좌/우 세로 변 처리 (꼭짓점 제외)
        for (int y = y1 + 1; y < y2; y++) {
            setEdge(x1, y, curIndex, 2, 4); // 왼쪽 변: 하, 상
            setEdge(x2, y, curIndex, 2, 4); // 오른쪽 변: 하, 상
        }
    }

    //꼭짓점 처리: 차단 검사 없이 두 방향을 강제로 켬
    private static void setCorner(int x, int y, int curIndex, int dir1, int dir2) {
        boolean[] checked = checkOutline(x, y, curIndex);
        if (!checked[0]) return;

        board[x][y][0] = 1;
        board[x][y][dir1] = 1;
        board[x][y][dir2] = 1;
    }

    //변 위의 점 처리: 두 방향을 켜되, 다른 사각형이 차단하는 방향은 다시 끔
    private static void setEdge(int x, int y, int curIndex, int dir1, int dir2) {
        boolean[] checked = checkOutline(x, y, curIndex);
        if (!checked[0]) return;

        board[x][y][0] = 1;
        board[x][y][dir1] = 1;
        board[x][y][dir2] = 1;

        // 차단된 방향은 다시 0으로
        for (int j = 0; j < 5; j++) {
            if (!checked[j]) board[x][y][j] = 0;
        }
    }

    public static boolean[] checkOutline(int x, int y, int curIndex) {
        boolean[] checkedDirections = new boolean[5];
        Arrays.fill(checkedDirections, true);

        for (int i = 0; i < rectangle.length; i++) {
            if (i == curIndex) continue;

            int rx1 = rectangle[i][0];
            int ry1 = rectangle[i][1];
            int rx2 = rectangle[i][2];
            int ry2 = rectangle[i][3];

            // 다른 직사각형 내부에 점이 있으면 둘레 아님
            if (x > rx1 && x < rx2 && y > ry1 && y < ry2) {
                Arrays.fill(checkedDirections, false);
                return checkedDirections;
            }

            // 다른 직사각형의 변 위에 점이 있을 때, 그 직사각형 내부로 진입하는 방향만 차단
            if (x == rx1 && y >= ry1 && y <= ry2) {
                checkedDirections[1] = false;  // 우 진입 차단
            }
            if (x == rx2 && y >= ry1 && y <= ry2) {
                checkedDirections[3] = false;  // 좌 진입 차단
            }
            if (y == ry1 && x >= rx1 && x <= rx2) {
                checkedDirections[4] = false;  // 상 진입 차단
            }
            if (y == ry2 && x >= rx1 && x <= rx2) {
                checkedDirections[2] = false;  // 하 진입 차단
            }
        }
        return checkedDirections;
    }
}
