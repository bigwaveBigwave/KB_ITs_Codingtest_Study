import java.util.*;

class Solution {
    static boolean[] visited;
    static ArrayList<Integer>[] adj_list;
    
    public int solution(int n, int[][] computers) {
        // 연결 요소의 개수 구하기
        // 방문여부 체크를 위한 visited 배열과, 인접 노드 확인을 위한 adj_list 선언
        visited = new boolean[n];
        adj_list = new ArrayList[n];
        int answer = 0;
        
        // ArrayList들로 이루어진 배열 초기화
        for (int i = 0; i < n; i++) {
            adj_list[i] = new ArrayList<Integer>();
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (computers[i][j] == 1) {
                    adj_list[i].add(j); //인접 노드 업데이트
                }
            }
        }
        
        // dfs를 활용해서 같은 네트워크 상의 노드는 visited로 표시
        // 따라서 새로운 노드를 탐색하게 된다면 새로운 네트워크 이므로 answer++
        for (int i = 0; i < n; i++) {
            if(!visited[i]) {
                answer++;
                dfs(i);
            }
        }
        
        return answer;
    }
    
    public static void dfs(int node) {
        visited[node] = true;
        
        for (int nextNode: adj_list[node]) {
            if (!visited[nextNode]) {
                dfs(nextNode);
            }
        }
    }
}
