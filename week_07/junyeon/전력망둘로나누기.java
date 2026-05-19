package week_07.junyeon;

import java.util.LinkedList;
import java.util.Queue;

public class 전력망둘로나누기 {
    Queue<Integer> queue = new LinkedList<>();
    public int solution(int n, int[][] wires) {
        int answer = n;
        int x;
        for (int i = 0 ; i < wires.length ; i++) {
            boolean[] visited = new boolean[n+1];
            if (i == 0) {
                x = wires[1][0];
            } else {
                x = wires[0][0];
            }
            visited[x] = true;
            queue.add(x);
            while (!queue.isEmpty()) {
                int k = queue.poll();
                bfs(k, visited, wires, i);
            }
            int a = 0;
            int b = 0;
            for (int j = 1 ; j < n+1 ; j++) {
                if(visited[j]==true) {
                    a += 1;
                }
            }
            b = n-a;
            int temp;
            if (a-b >= 0) {
                temp = a-b;
            } else {
                temp = b-a;
            }
            answer = answer > temp ? temp : answer;
        }
        return answer;
    }

    public void bfs(int x, boolean[] visited, int[][] wires, int w) {
        for (int i = 0 ; i < wires.length ; i++) {
            if (w==i) continue;
            int a = wires[i][0];
            int b = wires[i][1];
            if (a == x || b == x) {
                if (a == x && visited[b]==false) {
                    visited[b] = true;
                    queue.add(b);
                } else if (b==x && visited[a] == false) {
                    visited[a] = true;
                    queue.add(a);
                }
            }
        }
    }
}
