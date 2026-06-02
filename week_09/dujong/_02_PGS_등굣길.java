import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        // BFS? -> 최단거리를 구할 수는 있다, 그런데 최단거리 경로의 개수는?
        // 오른쪽 방향, 아래 방향만 사용
        // 어떤 위치까지 도달하는 경로가 최단경로가 아닌 경우는 없다
        // 각 위치까지 도달하는 경우의 수를 2차원 배열에 저장
        // dp[i][j] = dp[i][j-1] + dp[i-1][j]
        // dp[1][1~m] = 1, d[1~n][1] = 1
        // puddle이 위치한 곳은 초기값 0에서 업데이트하지 않고 건너뛰기
        
        long[][] board = new long[n+1][m+1];
        
        // 모두 1로 초기화
        for (int i = 0; i <= n; i++) {
            Arrays.fill(board[i], 1);
        }
        
        // puddle 위치는 0으로 업데이트
        // 만약 첫 행이나 열이었다면 이후 위치들 모두 0으로 업데이트
        for (int[] puddle: puddles) {
            int pRow = puddle[1];
            int pCol = puddle[0];
            
            board[pRow][pCol] = 0;
            if (pRow == 1) {
                for (int i = pCol + 1; i <= m; i++) {
                    board[1][i] = 0;
                }
            }
            if (pCol == 1) {
                for (int i = pRow + 1; i <= n; i++) {
                    board[i][1] = 0;
                }
            }
        }
        
        // dp 배열 업데이트
        for (int i = 2; i <= n; i++) {
            for (int j = 2; j <= m; j++) {
                if (board[i][j] == 0) continue;
                board[i][j] = (board[i-1][j] + board[i][j-1]) % 1_000_000_007;
            }
        }
        
        return (int)board[n][m];
    }
}
