import java.util.*;

class pg_섬연결하기 {

    public int findParent(int[] parent, int node) {
        if (parent[node] == node) {
            return node;
        }
        return parent[node] = findParent(parent, parent[node]);
    }

    public void union(int[] parent, int node1, int node2) {
        int root1 = findParent(parent, node1);
        int root2 = findParent(parent, node2);

        if(root1 < root2) {
            parent[root2] = root1;
        }else {
            parent[root1] = root2;
        }
    }

    public int solution(int n, int[][] costs) {
        int answer = 0;

        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));

        for(int[] edge : costs) {
            int node1 = edge[0];//연결할 섬
            int node2 = edge[1];//연결할 섬
            int cost = edge[2];//비용

            if (findParent(parent, node1) != findParent(parent, node2)) {
                answer += cost;
                union(parent, node1, node2);
            }
        }

        return answer;
    }
}