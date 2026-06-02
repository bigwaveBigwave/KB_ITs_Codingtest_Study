import java.util.*;
public class 셤연결 {
    int[] parent;

    public int find(int x) {
        if (parent[x]==x) return x;
        return parent[x] = find(parent[x]);
    }

    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootY] = rootX;
        }
    }

    public int solution(int n, int[][] costs) {
        int answer = 0;
        parent = new int[n];


        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }


        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));


        for (int[] edge : costs) {
            int from = edge[0];
            int to = edge[1];
            int cost = edge[2];


            if (find(from) != find(to)) {
                union(from, to);
                answer += cost;
            }
        }

        return answer;
    }
}
