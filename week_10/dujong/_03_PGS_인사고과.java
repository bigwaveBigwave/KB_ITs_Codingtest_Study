import java.util.*;

class Solution {
    public int solution(int[][] scores) {
        // 근무 태도 점수, 동료 평가 점수
        // 모두 어떤 사원보다 낮으면 인센티브 X
        // 두 점수의 합이 높은 순서대로 인센티브 차등 지급
        // 1, 1, 3, 4, ...
        // 완호의 석차 구하기
        
        // 인센티브를 받지 못하는 사람을 미리 빼 놓아야 석차를 구하기 편하긴 하다
        // 매번 모든 사람과 비교하면 좋겠지만, O(N^2) 은 사용 불가
        // 점수1 을 기준으로 내림차순 정렬, 같으면 점수2 기준으로는 오름차순 정렬
        // -> 이후에 점수2에 대해서 이전의 max값보다 작으면 제외
        
        int wonhoScore1 = scores[0][0];
        int wonhoScore2 = scores[0][1];
        int wonhoSum = wonhoScore1 + wonhoScore2;
        
        Arrays.sort(scores, (a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            }
            return b[0] - a[0];
        });
        
        List<int[]> validScores = new ArrayList<>();
        int maxScore2 = -1;
        
        for (int i = 0; i < scores.length; i++) {
            if (scores[i][1] >= maxScore2) {
                maxScore2 = scores[i][1];
                validScores.add(scores[i]);
            }
        }
        
        Collections.sort(validScores, (a, b) -> {
            return (b[0] + b[1]) - (a[0] + a[1]);
        });
        
        for (int i = 0; i < validScores.size(); i++) {
            if (validScores.get(i)[0] == wonhoScore1 && validScores.get(i)[1] == wonhoScore2) {
                int pos = -1;
                for (pos = i - 1; pos >= 0; pos--) {
                    if (validScores.get(pos)[0] + validScores.get(pos)[1] != wonhoSum) {
                        break;
                    }
                }
                return pos + 2;
            }
        }
        
        return -1;
    }
}
