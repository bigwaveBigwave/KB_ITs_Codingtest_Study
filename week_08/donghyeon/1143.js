/**
 * @param {string} text1
 * @param {string} text2
 * @param {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    const m = text1.length;
    const n = text2.length;
    
    // (m + 1) x (n + 1) 크기의 2차원 배열을 0으로 초기화
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    
    // 반복문을 돌며 DP 테이블 채우기
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i - 1] === text2[j - 1]) {
                // 두 문자가 같다면 대각선 왼쪽 위 값에 1을 더함
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // 두 문자가 다르다면 위쪽 값과 왼쪽 값 중 큰 값을 가져옴
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // 가장 마지막 칸에 최장 공통 부분 수열의 길이가 저장됨
    return dp[m][n];
};
