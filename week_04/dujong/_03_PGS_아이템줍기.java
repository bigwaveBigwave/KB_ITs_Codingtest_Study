import java.util.*;

class Solution {
    static int[][][] board;
    static int[][] rectangle;
    static boolean[][] visited;
    static int answer;

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        // 최단거리 -> BFS
        /*
        접근 1. 각 직사각형의 둘레에 존재하는 점들을 ArrayList에 넣고, 새로운 직사각형이 들어올 때마다 업데이트
            -> 이 경우 나중에 최단거리를 찾는데 어려움이 있을 것으로 예상
        접근 2. 좌표값의 상한선이 50이므로, 전체 board를 선언하고 유효한 값들을 true로 설정
            -> 추후에 BFS로 탐색하기 용이
        */

        // 1. 초기화
        Solution.rectangle = rectangle;
        board = new int[51][51][5];
        visited = new boolean[51][51];
        answer = 0;

        // 2. 각 직사각형의 테두리에 있는 모든 점들을 순회하면서 유효한 위치와 방향 저장
        // board[x][y][] 에서 마지막 배열에 {위치 유효여부, 오른쪽, 아래쪽, 왼쪽, 위쪽} 순서대로 유효성 저장
        // 방향 인덱스: 1=우, 2=하, 3=좌, 4=상
        // 유효한 경우 = 1, 유효하지 않은 경우 = 0
        for (int i = 0; i < rectangle.length; i++) {
            setValidCoordinates(rectangle[i], i);
        }

        // 3. bfs를 이용해서 board를 순회
        bfs(characterX, characterY, itemX, itemY);

        return answer;
    }

    public static void bfs(int startX, int startY, int targetX, int targetY) {
        Queue<int[]> myQueue = new ArrayDeque<>();
        visited[startX][startY] = true;
        myQueue.offer(new int[] {startX, startY, 0}); //마지막 숫자는 depth

        while (!myQueue.isEmpty()) {
            int[] curPos = myQueue.poll();
            int curX= curPos[0];
            int curY = curPos[1];
            int depth = curPos[2];

            // 4. 종료조건: target 위치에 도달한 경우
            if (curX == targetX && curY == targetY) {
                answer = depth;
                break;
            }

            int[] validDirections = board[curX][curY];

            // 우, 하, 좌, 상 위치 중에서 유효한 방향이 있다면 해당 위치 탐색
            for (int i = 1; i <= 4; i++) {
                int newX = curX;
                int newY = curY;

                if (validDirections[i] == 1) {
                    switch (i) {
                        case 1:
                            newX = curX + 1;
                            break;
                        case 3:
                            newX = curX - 1;
                            break;
                        case 2:
                            newY = curY - 1;
                            break;
                        case 4:
                            newY = curY + 1;
                            break;
                    }

                    if (!visited[newX][newY]) {
                        visited[newX][newY] = true;
                        myQueue.offer(new int[] {newX, newY, depth + 1});
                    }
                }
            }
        }
    }

    public static void setValidCoordinates(int[] rectPos, int curIndex) {
        int x1 = rectPos[0];
        int y1 = rectPos[1];
        int x2 = rectPos[2];
        int y2 = rectPos[3];
        boolean[] checkedDirections;

        // 2-1. 꼭짓점 위치 유효성 및 방향 유효성 설정
        checkedDirections = checkOutline(x1, y1, curIndex);
        if (checkedDirections[0]) {
            board[x1][y1][0] = 1;
            board[x1][y1][1] = 1;
            board[x1][y1][4] = 1;
        }

        checkedDirections = checkOutline(x2, y1, curIndex);
        if (checkedDirections[0]) {
            board[x2][y1][0] = 1;
            board[x2][y1][3] = 1;
            board[x2][y1][4] = 1;
        }

        checkedDirections = checkOutline(x1, y2, curIndex);
        if (checkedDirections[0]) {
            board[x1][y2][0] = 1;
            board[x1][y2][1] = 1;
            board[x1][y2][2] = 1;
        }

        checkedDirections = checkOutline(x2, y2, curIndex);
        if (checkedDirections[0]) {
            board[x2][y2][0] = 1;
            board[x2][y2][3] = 1;
            board[x2][y2][2] = 1;
        }

        // 2-2. 위/아래 가로 변 처리 (꼭짓점 제외)
        for (int i = x1 + 1; i < x2; i++) {
            checkedDirections = checkOutline(i, y1, curIndex);
            if (checkedDirections[0]) {
                board[i][y1][0] = 1;
                board[i][y1][1] = 1;
                board[i][y1][3] = 1;
                for (int j = 1; j <= 4; j++) {
                    if (checkedDirections[j] == false) {
                        board[i][y1][j] = 0;
                    }
                }
            }

            checkedDirections = checkOutline(i, y2, curIndex);
            if (checkedDirections[0]) {
                board[i][y2][0] = 1;
                board[i][y2][1] = 1;
                board[i][y2][3] = 1;
                for (int j = 1; j <= 4; j++) {
                    if (checkedDirections[j] == false) {
                        board[i][y2][j] = 0;
                    }
                }
            }
        }

        // 2-3. 좌/우 세로 변 처리 (꼭짓점 제외)
        for (int i = y1 + 1; i < y2; i++) {
            checkedDirections = checkOutline(x1, i, curIndex);
            if (checkedDirections[0]) {
                board[x1][i][0] = 1;
                board[x1][i][2] = 1;
                board[x1][i][4] = 1;
                for (int j = 1; j <= 4; j++) {
                    if (checkedDirections[j] == false) {
                        board[x1][i][j] = 0;
                    }
                }
            }
            checkedDirections = checkOutline(x2, i, curIndex);
            if (checkedDirections[0]) {
                board[x2][i][0] = 1;
                board[x2][i][2] = 1;
                board[x2][i][4] = 1;
                for (int j = 1; j <= 4; j++) {
                    if (checkedDirections[j] == false) {
                        board[x2][i][j] = 0;
                    }
                }
            }
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
