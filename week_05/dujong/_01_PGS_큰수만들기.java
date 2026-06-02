import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Deque<Integer> dq = new ArrayDeque<>(); // 숫자들 임시 저장
        
        for (int i = 0; i < number.length(); i++) {
            int curNum = number.charAt(i) - '0';
            
            // 현재 숫자가 이전 숫자보다 커지는 경우, 이전에 내림차순으로 저장된 숫자들도 순차적으로 비교해서 삭제
            while (!dq.isEmpty() && k > 0 && dq.peekLast() < curNum) {
                dq.pollLast();
                k--;
            }
            
            // 현재 숫자 추가
            dq.offerLast(curNum);
        }
        
        // 아직 삭제할 숫자가 남은 경우
        while (k > 0) {
            dq.pollLast();
            k--;
        }
        
        StringBuilder sb = new StringBuilder();

        while (!dq.isEmpty()) {
            sb.append(dq.pollFirst());
        }
        
        return sb.toString();
    }
}
