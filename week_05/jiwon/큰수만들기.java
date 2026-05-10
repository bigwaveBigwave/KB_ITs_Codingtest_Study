import java.util.*;

class Solution {
    public String solution(String number, int k) {

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < number.length(); i++) {

            char current = number.charAt(i);

            // 앞자리에 가장 큰 수 오도록 작은 수 제거 
            while (!stack.isEmpty() && k > 0 && stack.peek() < current) {
                stack.pop();
                k--;
            }

            stack.push(current);
        }

        // 내림차순 정렬되어있고, 아직 k 남은 경우 -> 뒤에서 제거
        while (k > 0) {
            stack.pop();
            k--;
        }

        StringBuilder sb = new StringBuilder();

        for (char c : stack) {
            sb.append(c);
        }

        return sb.toString();
    }
}