package PG;

import java.util.Stack;

public class pg_택배상자 {

    public int solution(int[] order) {
        Stack<Integer> sub = new Stack<>();
        int answer = 0;
        int idx = 0; // 실제 담겨있는 박스 번호

        for(int i=1; i<=order.length; i++){
            if(i != order[idx] ){
                sub.push(i);
            }else{
                idx++;
                answer++;
            }

            while(!sub.isEmpty() && sub.peek() == order[idx]){
                sub.pop();
                idx++;
                answer++;
            }
        }

        return answer;
    }
}
