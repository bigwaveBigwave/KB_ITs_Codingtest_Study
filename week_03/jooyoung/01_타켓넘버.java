import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;

        Deque<int[]> stack = new ArrayDeque<>();

        stack.push(new int[]{0, 0});

        while (!stack.isEmpty()) {
            int[] current = stack.pop();
            int index = current[0];
            int sum = current[1];

            // 숫자를 다 썼으면
            if (index == numbers.length) {
                if (sum == target) {
                    answer++;
                }
                continue;
            }

            // + 붙인 경우
            stack.push(new int[]{index + 1, sum + numbers[index]});

            // - 붙인 경우
            stack.push(new int[]{index + 1, sum - numbers[index]});
        }

        return answer;
    }
}