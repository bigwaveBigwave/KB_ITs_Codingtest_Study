import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        // 오름차순 정렬
        Arrays.sort(routes, (int[] a, int[] b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            }
            return a[0] - b[0];
        });
        
        // 투포인터를 활용해서 startIndex가 기존 endIndex보다 커지는 경우 answer++
        int startIndex = -30001;
        int endIndex = 30001;
        int answer = 1;
        
        for (int i = 0; i < routes.length; i++) {
            // startIndex는 큰 값 기준 업데이트
            if (routes[i][0] > startIndex) {
                startIndex = routes[i][0];
            }
            
            // endIndex는 작은 값 기준 업데이트
            if (routes[i][1] < endIndex) {
                endIndex = routes[i][1];
            }
            
            // 단속카메라 추가
            if (endIndex < startIndex) {
                answer++;
                endIndex = routes[i][1];
            }
        }
        
        return answer;
    }
}
