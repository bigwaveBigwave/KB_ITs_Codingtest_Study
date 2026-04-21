import java.util.Stack;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            // 아직 방문 안 한 컴퓨터면 새로운 네트워크 시작
            if (!visited[i]) {
                answer++;
                stack.push(i);

                // 스택이 빌 때까지 같은 네트워크 탐색
                while (!stack.isEmpty()) {
                    int current = stack.pop();

                    // 이미 방문한 적 있으면 넘어감
                    if (visited[current]) {
                        continue;
                    }

                    // 현재 컴퓨터 방문 처리
                    visited[current] = true;

                    // current와 연결된 컴퓨터들 확인
                    for (int j = 0; j < n; j++) {
                        if (computers[current][j] == 1 && !visited[j]) {
                            stack.push(j);
                        }
                    }
                }
            }
        }

        return answer;
    }
}