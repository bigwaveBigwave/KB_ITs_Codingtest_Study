class Solution {
    public int solution(int[][] triangle) {
        /*
        7
        3 8
        8 1 0
        2 7 4 4
        4 5 2 6 5
        
        7
        10 15
        18 16 15
        20 25 20 19
        24 30 27 26 24
        */
        // 만들어질 수 있는 정수의 최대 한도: 500 * 9999 = 대략 5,000,000 -> int 사용가능
        // Top-Down 으로 dp 배열 계산
        // dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        // 마지막 행의 값들 중 최대값 구하기
        
        int n = triangle.length;
        int[][] dp = new int[n][];
        
        for (int i = 0; i < n; i++) {
            dp[i] = new int[i+1];
        }
        
        dp[0][0] = triangle[0][0];
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i-1][j] + triangle[i][j];
                }
                else if (j == i) {
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j];
                }
                else {
                    dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
                }
            }
        }
        
        int answer = -1;
        for (int num: dp[n-1]) {
            if (num > answer) answer = num;
        }
        
        return answer;
    }
}
