import java.util.*;

public class bj_2504 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.next(); //괄호 문자열 받기

        Stack<Character> stack = new Stack<>();
        int value = 1;
        int result = 0;

        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i); //괄호를 하나씩 받아오기

            if (c == '(') {
                stack.push(c);
                value *= 2;
            } else if (c == '[') {
                stack.push(c);
                value *= 3;
            } else if (c == ')') {
                if (stack.isEmpty() || stack.peek() != '(') {
                    result = 0;
                    break;
                }
                if (s.charAt(i - 1) == '(') result += value;
                stack.pop();
                value /= 2;
            } else if (c == ']') {
                if (stack.isEmpty() || stack.peek() != '[') {
                    result = 0;
                    break;
                }
                if (s.charAt(i - 1) == '[') result += value;
                stack.pop();
                value /= 3;
            }
        }
        if (!stack.isEmpty()) System.out.println(0);
        else System.out.println(result);
    }
}
