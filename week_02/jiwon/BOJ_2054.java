package week_02.jiwon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class BOJ_2054 {
     public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        ArrayDeque<String> stack = new ArrayDeque<>();

        // 스택에 넣기 시작
        for(char c : line.toCharArray()) {
            String cur = String.valueOf(c);

            if(cur.equals("(") || cur.equals("[")) {
                // 열림 괄호 -> push
                stack.push(cur);
            } else if(cur.equals(")")) {
                /*
                닫힘 괄호
                - 스택 비어있거나 열림 괄호와 매치 안되는 경우: 0 출력
                - top이 ( 인 경우: 스택에 2 push
                - top이 숫자인 경우:
                    - pop 하면서 숫자끼리 더해서 tmp에 저장
                    - 열림 괄호 만나면 곱하기 연산 후 스택에 push 
                */

                int tmp = 0;

                if(stack.isEmpty() || stack.peek().equals("[")) {
                    System.out.println("0");
                    return;
                } else if(stack.peek().equals("(")) {
                    stack.pop();
                    stack.push("2");
                } else {
                    while (!stack.isEmpty()) {
                        String top = stack.peek();

                        // 1. top이 ( : 숫자 합치기 그만
                        if(top.equals("(")) break;
                        else if(top.equals("[")) {
                            // 2. top이 [ : 올바르지 못한 괄호
                            System.out.println("0");
                            return;
                        }

                        // 3. top이 숫자 : pop 후 tmp에 더함 
                        tmp += Integer.parseInt(stack.pop());
                    }

                    if(!stack.isEmpty() && stack.peek().equals("(")) {
                        stack.pop();
                        stack.push(String.valueOf(tmp*2));
                    } else {
                        System.out.println("0");
                        return;
                    }
                }
            } else if(cur.equals("]")) {
                // ) 와 같은 로직
                
                int tmp = 0;

                if(stack.isEmpty() || stack.peek().equals("(")) {
                    System.out.println("0");
                    return;
                } else if(stack.peek().equals("[")) {
                    stack.pop();
                    stack.push("3");
                } else {
                    while (!stack.isEmpty()) {
                        String top = stack.peek();

                        if(top.equals("[")) break;
                        else if(top.equals("(")) {
                            System.out.println("0");
                            return;
                        }

                        tmp += Integer.parseInt(stack.pop());
                    }

                    if(!stack.isEmpty() && stack.peek().equals("[")) {
                        stack.pop();
                        stack.push(String.valueOf(tmp*3));
                    } else {
                        System.out.println("0");
                        return;
                    }
                }
            }
        }

        int answer = 0;
        while (!stack.isEmpty()) {
            if(stack.peek().equals("(") || stack.peek().equals("[")) {
                // 스택에 괄호 남아있으면 올바르지 못한 괄호 
                System.out.println("0");
                return;
            } else {
                answer += Integer.parseInt(stack.pop());
            }  
        }
        System.out.println(answer);
     }
}
