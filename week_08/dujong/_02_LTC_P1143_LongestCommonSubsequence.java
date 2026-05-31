class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // 2차원 배열을 활용해서 현재 문자와 대응되는 문자가 같은지 다른지 판단

        int n = text1.length();
        int m = text2.length();
        int[][] D = new int[n+1][m+1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (text1.charAt(i-1) == text2.charAt(j-1)) {
                    D[i][j] = D[i-1][j-1] + 1;
                } else {
                    D[i][j] = Math.max(D[i-1][j], D[i][j-1]);
                }
            }
        }

        return D[n][m];
    }
}
