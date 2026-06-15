package PG;

import java.util.Arrays;

public class pg_인사고과 {
    public int solution(int[][] scores) {
        int answer = 0;
        int wanho_a = scores[0][0];
        int wanho_b = scores[0][1];
        int wanho_sum = wanho_a + wanho_b;
        int max = 0;
        int rank = 1;

        Arrays.sort(scores, (a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1]; //근무 태도가 같으면 동료 평가는 오름차순
            } else {
                return b[0] - a[0]; //근무 태도가 다르면 내림차순
            }
        });

        for(int i=0; i<scores.length; i++){
            int a = scores[i][0];
            int b = scores[i][1];

            if(b < max){
                if(a == wanho_a && b == wanho_b){
                    return -1;
                }
                continue;
            }

            max = Math.max(max, b);

            if (a + b > wanho_sum) {
                rank++;
            }
        }


        return rank;
    }
}
