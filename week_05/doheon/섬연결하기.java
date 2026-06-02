import java.util.*;

class Solution {
    static int[] parent;

    public int solution(int n, int[][] costs) {
        int answer = 0;
        int edgeCount = 0;


        Arrays.sort(costs, (a, b) -> a[2] - b[2]);


        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }


        for (int[] cost : costs) {
            int islandA = cost[0];
            int islandB = cost[1];
            int bridgeCost = cost[2];


            if (find(islandA) != find(islandB)) {
                union(islandA, islandB);
                answer += bridgeCost;
                edgeCount++;
            }


            if (edgeCount == n - 1) {
                break;
            }
        }

        return answer;
    }

    static int find(int x) {
        if (parent[x] == x) {
            return x;
        }

        return parent[x] = find(parent[x]);
    }

    static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA != rootB) {
            parent[rootB] = rootA;
        }
    }
}