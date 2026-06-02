package PG;

public class pg_등굣길 {
    public int solution(int m, int n, int[][] puddles) {
        int dp[][] = new int[n+1][m+1];
        int mod = 1000000007;

        dp[1][1] = 1; //시작지점 초기화

        for(int []puddle: puddles){ //웅덩이는 -1로 설정
            dp[puddle[1]][puddle[0]] = -1;
        }

        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                if(i == 1 && j == 1){//시작지점은 이미 1로 초기화해서 건너뜀
                    continue;
                }

                if(dp[i][j] == -1){//웅덩이를 만난다면
                    dp[i][j] = 0;
                    continue;
                }

                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod;
            }
        }
        int answer = dp[n][m];
        return answer;
    }
}
