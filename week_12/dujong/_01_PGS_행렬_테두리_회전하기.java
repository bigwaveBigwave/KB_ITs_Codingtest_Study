import java.util.*;

class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        //문제에서 주어진대로 구현하기
        //2차원배열에 매번 변경되는 위치 업데이트 하기
        
        int[][] board = new int[rows][columns];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                board[i][j] = columns * i + (j + 1);
            }
        }
        
        Queue<int[]> queue = new ArrayDeque<>();
        int[] answer = new int[queries.length];
        Arrays.fill(answer, rows * columns + 1);
        
        for (int qIndex = 0; qIndex < queries.length; qIndex++) {
            int[] query = queries[qIndex];
            int x1 = query[0]; int y1 = query[1];
            int x2 = query[2]; int y2 = query[3];
            
            for (int i = x1 - 1; i < x2; i++) {
                for (int j = y1 - 1; j < y2; j++) {
                    if (i == x1 - 1) { //위쪽 가로줄
                        if (j == y1 - 1) {
                            queue.offer(new int[] {board[i + 1][j], i, j});
                        }
                        else {
                            queue.offer(new int[] {board[i][j - 1], i , j});
                        }
                    }
                    else if (i == x2 - 1) { //아래쪽 가로줄
                        if (j == y2 - 1) {
                            queue.offer(new int[] {board[i - 1][j], i, j});
                        }
                        else {
                            queue.offer(new int[] {board[i][j + 1], i, j});
                        }
                    }
                    else { //양옆 모서리
                        if (j == y1 - 1) {
                            queue.offer(new int[] {board[i + 1][j], i, j});
                        }
                        else if (j == y2 - 1) {
                            queue.offer(new int[] {board[i - 1][j], i, j});
                        }
                    }
                }
            }
            
            while (!queue.isEmpty()) {
                int[] valPos = queue.poll();
                answer[qIndex] = Math.min(answer[qIndex], valPos[0]);
                board[valPos[1]][valPos[2]] = valPos[0];
            }
        }

        return answer;
    }
}
