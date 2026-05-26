class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # padding을 위해 (m+1) x (n+1) 크기의 DP 테이블을 0으로 초기화
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # DP 테이블 채우기
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 문자가 같으면 대각선 왼쪽 위 값 + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 문자가 다르면 위쪽과 왼쪽 값 중 큰 값
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        
        return dp[m][n]