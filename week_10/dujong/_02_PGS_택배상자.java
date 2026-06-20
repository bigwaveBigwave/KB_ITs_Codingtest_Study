import java.util.*;

class Solution {
    public int solution(int[] order) {
        // 보조 컨테이너 벨트: LIFO (스택)
        // 4 3 1 2 5
        
        Deque<Integer> stack = new ArrayDeque<>();
        int answer = 0; // 실을 수 있는 상자수
        int incNum = 0; // 오름차순 자연수
        
        for (int cur: order) {
            while (cur > incNum) {
                incNum++;
                stack.push(incNum);
            }
            if (stack.peek() == cur) {
                stack.pop();
                answer++;
            }
            else {
                break;
            }
        }
        
        return answer;
    }
}
