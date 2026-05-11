import java.util.*;

class Solution {
    static ArrayList<int[]>[] adj_list;
    static boolean[] visited;
    static int answer;
    
    public int solution(int n, int[][] costs) {
        // 문제의 조건이 헷갈린다
        // 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다. -> 간선이 없는 두 노드는 직접 연결은 불가능하다는 것
        // 연결할 수 없는 섬은 주어지지 않습니다. -> 하나의 Connected Component로 표현 가능하다는 것
        
        answer = 0;
        visited = new boolean[n];
        
        // 인접 리스트 초기화
        adj_list = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj_list[i] = new ArrayList<int[]>();
        }
        
        // 인접 리스트 업데이트 (가중치 포함)
        for (int i = 0; i < costs.length; i++) {
            int node1 = costs[i][0];
            int node2 = costs[i][1];
            int weight = costs[i][2];
            
            adj_list[node1].add(new int[] {node2, weight});
            adj_list[node2].add(new int[] {node1, weight});
        }
        
        visited[0] = true;
        
        // 간선 추가하기
        for (int i = 0; i < n - 1; i++) {
            int minCost = Integer.MAX_VALUE;
            int nextNode = -1;
            
            // 현재 추가된 노드들에서 뻗어나가는 간선 중 최소값 찾기
            for (int j = 0; j < n; j++) {
                if (!visited[j]) continue;
                for (int[] adj_node: adj_list[j]) {
                    int vertex = adj_node[0];
                    int weight = adj_node[1];
                    if (!visited[vertex] && weight < minCost) {
                        minCost = weight;
                        nextNode = vertex;
                    }
                }
            }
            
            answer += minCost;
            visited[nextNode] = true;
        }
            
        return answer;
    }
}
