import java.util.*;

class Solution {
    public String removeKdigits(String num, int k) {

        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < num.length(); i++) {
            char cur = num.charAt(i);

            // 앞자리에 작은 수 오도록 - 0은 패스
            while(!stack.isEmpty() && k > 0 && stack.peek() > cur && stack.peek() != '0') {
                stack.pop();
                k--;
            }

            stack.push(cur);
        }
        
        while(k > 0) {
            stack.pop();
            k--;
        }

        StringBuilder sb = new StringBuilder();

        for (char c : stack) {
            sb.append(c);
        }

        // 앞쪽에 채워진 0 지워서 출력
        int idx = 0;

        while(idx < sb.length() && sb.charAt(idx) == '0') {
            idx++;
        }

        // 비어있는 경우 "0" 출력
        if(sb.length() == idx) {
            return "0";
        }
        
        return sb.substring(idx);
    }
}