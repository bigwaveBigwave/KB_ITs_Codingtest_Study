import java.util.*;

class Solution {
    int answer;
    List<List<Integer>> adj_list;
    
    public int solution(int n, int[][] wires) {
        // 전력망별 송전탑의 개수를 최대한 비슷하게 맞추기
        // 주어진 간선 리스트를 기반으로 노드 기준의 인접 리스트 만들기
        // 만들어진 인접 리스트에서 각 간선을 없애면서 노드1 쪽의 개수와 노드2쪽의 개수 비교
        // Math.min() 으로 전역변수 업데이트
        // 모든 간선을 없애봤다면 -> return answer
        
        answer = n;
        adj_list = new ArrayList<>(n+1);
        boolean[] visited = new boolean[n+1];
        
        for (int i = 0; i < n+1; i++) {
            adj_list.add(new ArrayList<>());
        }
        
        // 인접리스트 업데이트
        for (int[] wire: wires) {
            int node1 = wire[0];
            int node2 = wire[1];
            adj_list.get(node1).add(node2);
            adj_list.get(node2).add(node1);
        }
        
        // 송전탑 개수 차이 최솟값 찾기
        for (int[] wire: wires) {
            int node1 = wire[0];
            int node2 = wire[1];
            adj_list.get(node1).remove(Integer.valueOf(node2));
            adj_list.get(node2).remove(Integer.valueOf(node1));
            
            int cnt1 = dfs(node1, visited);
            int cnt2 = dfs(node2, visited);
            answer = Math.min(answer, Math.abs(cnt1 - cnt2));
            Arrays.fill(visited, false);
            
            adj_list.get(node1).add(node2);
            adj_list.get(node2).add(node1);
        }
        
        return answer;
    }
    
    private int dfs(int curNode, boolean[] visited) {
        visited[curNode] = true;
        int count = 1;
        
        for (int nextNode: adj_list.get(curNode)) {
            if (!visited[nextNode]) {
                count += dfs(nextNode, visited);
            }
        }
        
        return count;
    }
}
