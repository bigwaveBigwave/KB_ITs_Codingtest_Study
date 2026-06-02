class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        # DP 테이블 초기화(인덱스를 n과 맞추기 위해 n+1 크기로 생성)
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # 3번째 계단부터 n번쨰 계단까지 점화식 사용
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
