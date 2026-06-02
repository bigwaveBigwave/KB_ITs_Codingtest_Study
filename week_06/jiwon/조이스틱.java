// 연속된 A가 있는 경우를 고려하기

class Solution {
    public int solution(String name) {
        int answer = 0;
        int len = name.length();
        
        // 좌우 이동 횟수 초기화 (계속 오른쪽으로 이동하는 경우)
        int move = len -1;
        
        for(int i=0; i < len; i++) {
            
            char c = name.charAt(i);
            
            // 알파벳 변경 횟수
            answer += Math.min(c - 'A', 'Z' - c + 1);
            
            // 좌우 이동 횟수
            // next = 현재 위치 다음부터 연속된 A 끝 찾기
            int next = i+1;
            
            while(next < len && name.charAt(next) == 'A') {
                next++;
            }

            // 1. 오른쪽으로 갔다가 처음으로 다시 돌아오는 경우
            move = Math.min(move, i * 2 + (len - next));

            // 2. 끝으로 갔다가 다시 앞쪽으로 돌아오는 경우 
            move = Math.min(move, (len - next) * 2 + i);
        }
        
        return answer + move;
    }
}