class Solution {
    public int solution(String name) {
        int N = name.length();
        int answer = 0;
        
        // 위아래 이동
        for (int i = 0; i < N; i++) {
            char curChar = name.charAt(i);
            if (curChar != 'A'){
                int distH = Math.min(curChar - 'A', 'Z' - curChar + 1);
                answer += distH;
            }
        }
        
        // 좌우 이동 (모든 위치에서 최선의 이동 경로 업데이트)
        int distW = N - 1;
        for (int i = 0; i < N; i++) {
            // 현재 위치에서 오른쪽으로 가장 가까운 'A'가 아닌 위치 찾기
            int next = i + 1;
            while (next < N && name.charAt(next) == 'A') {
                next++;
            }
            
            // 오른쪽으로 i까지 갔다가 -> 왼쪽으로 돌아서 -> next까지 거리
            distW = Math.min(distW, 2 * i + (N - next));
                
            // 왼쪽으로 next까지 갔다가 -> 오른쪽으로 돌아서 -> i까지 거리
            distW = Math.min(distW, 2 * (N - next) + i);
        }
        answer += distW;
        
        return answer;
    }
}
