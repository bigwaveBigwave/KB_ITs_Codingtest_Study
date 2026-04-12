//import java.util.*;
//
//public class bj_1874 {
//    public static void main(String[] args) {
//
//        Scanner sc = new Scanner(System.in);
//        StringBuilder sb = new StringBuilder();
//        Stack<Integer> stack = new Stack<>();
//
//        int n = sc.nextInt();
//        int current = 1;
//
//        for (int i = 1; i <= n; i++) {
//            int target = sc.nextInt();
//
//            while (current <= target) {
//                stack.push(current);
//                sb.append("+\n");
//                current++;
//            }
//
//            if (stack.peek() == target) {
//                stack.pop();
//                sb.append("-\n"); // 꺼냈으니 - 저장
//            }
//            else {
//                System.out.println("NO"); // 지체 없이 NO 출력
//                return;
//            }
//        }
//        System.out.println(sb);
//    }
//}