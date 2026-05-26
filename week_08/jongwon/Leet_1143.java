package LEET;

import java.util.*;

class Leet_1143 {
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();

        int[][] dp = new int[n+1][m+1]; //공백을 포함하기 위해 +1을 해줌

        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                if(text1.charAt(i-1) == text2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1] + 1; //대각선 왼쪽 위 값
                }else{
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]); //위쪽, 왼쪽 중 더 큰값을 지정
                }
            }
        }
        return dp[n][m];
    }
}