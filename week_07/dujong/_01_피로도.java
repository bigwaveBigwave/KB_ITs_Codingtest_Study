import java.util.*;

class Solution {
    int answer;
    
    public int solution(int k, int[][] dungeons) {
        // 그리디? -> no
        // 던전의 개수가 8 이하 -> 완전탐색 가능 (8!)
        answer = 0;
        boolean[] visited = new boolean[dungeons.length];
        
        backtrack(0, k, dungeons, visited);
        
        return answer;
    }
    
    private void backtrack(int depth, int hp, int[][] dungeons, boolean[] visited) {
        answer = Math.max(answer, depth);
        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && hp >= dungeons[i][0]) {
                visited[i] = true;
                backtrack(depth + 1, hp - dungeons[i][1], dungeons, visited);
                visited[i] = false;
            }
        }
    }
}
