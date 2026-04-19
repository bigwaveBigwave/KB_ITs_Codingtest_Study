import java.util.*;
class Network {
    Queue<Integer> queue = new LinkedList<>();

    public void bfs(int start, boolean[] visited, int[][] computers) {
        visited[start] = true;

        for (int i = 0 ; i < computers.length ; i++) {
            if (computers[start][i] == 1 && visited[i]==false) {
                visited[i] = true;
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int s = queue.poll();
            bfs(s, visited, computers);
        }
    }

    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[computers.length];
        for (int i = 0 ; i < computers.length ; i++) {
            if (visited[i]==false) {
                answer += 1;
                bfs(i, visited, computers);
            }
        }

        return answer;
    }
}
