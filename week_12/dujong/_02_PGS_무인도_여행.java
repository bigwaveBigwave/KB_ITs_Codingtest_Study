import java.util.*;

class Solution {
    private boolean[][] visited;
    private int[][] board;
    private int[] dr = {1, 0, -1, 0};
    private int[] dc = {0, 1, 0, -1};
    private int N;
    private int M;
    
    public List<Integer> solution(String[] maps) {
        //bfs로 섬 파악하기
        N = maps.length;
        M = maps[0].length();
        
        visited = new boolean[N][M];
        board = new int[N][M];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (maps[i].charAt(j) != 'X') {
                    board[i][j] = maps[i].charAt(j) - '0';
                }
            }
        }
        
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 0 ; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j] && board[i][j] > 0) {
                    answer.add(bfs(i, j));
                }
            }
        }
        
        if (answer.isEmpty()) {
            answer.add(-1);
        } else {
            Collections.sort(answer);
        }
        
        return answer;
    }
    
    private int bfs(int startR, int startC) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {startR, startC});
        visited[startR][startC] = true;
        int totalDays = board[startR][startC];
            
        while (!queue.isEmpty()) {
            int[] curPos = queue.poll();
            
            for (int i = 0; i < 4; i++) {
                int nr = curPos[0] + dr[i];
                int nc = curPos[1] + dc[i];
                
                if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                    continue;
                }
                
                if (!visited[nr][nc] && board[nr][nc] > 0) {
                    queue.offer(new int[] {nr, nc});
                    visited[nr][nc] = true;
                    totalDays += board[nr][nc];
                }
            }
            
        }
            
        return totalDays;
    }
}
