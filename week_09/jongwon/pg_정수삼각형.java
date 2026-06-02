package PG;

public class pg_정수삼각형 {
        public int solution(int[][] triangle) {
            int n = triangle.length;
            int[][] dp = new int[n][n];
            int answer = 0;

            dp[0][0] = triangle[0][0];

            for(int i=1; i<n; i++){
                for(int j=0; j<=i; j++){
                    if(j == 0){//맨 왼쪽일때
                        dp[i][j] = dp[i-1][j] + triangle[i][j];//위칸에 현재칸 숫자 더하기
                    }else if(j==i){//맨끝
                        dp[i][j] = dp[i-1][j-1] + triangle[i][j]; //왼쪽위칸 현재칸 숫자 더하기
                    }else{//가운데 칸들
                        dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]; //왼쪽위와 오른쪽위 중 더 큰값과 현재칸 더하기
                    }
                }
            }
            for(int j=0; j<n; j++){
                answer = Math.max(answer, dp[n-1][j]);
            }
            return answer;
        }

}
