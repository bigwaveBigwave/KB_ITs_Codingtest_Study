class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # dp[i]는 i원을 만드는 데에 필요한 동전의 최소 개수
        # 금액이 amount일 때 최소 동전 개수는 아무리 많아도 amount를 넘을 수 없음
        # 최댓값 대용으로 임의의 큰 값(amount + 1)로 초기화
        dp = [amount + 1] * (amount + 1)

        # 0원을 만드는 데 필요한 동전은 0개
        dp[0] = 0

        # 1원부터 목표 금액(amount)까지 차례대로 최소 동전 개수를 구학
        for i in range(1, amount + 1):
            for coin in coins:
                # 현재 계산하려는 금액 i가 동전의 액면가보다 크거나 같아야만
                # 그 동전을 사용할 수 있음
                if i - coin >= 0:
                    # 기존 dp[i]값과 i-coin 원을 만들었을 때의 최소 개수에 동전 1개를
                    # 더한 값 중 더 작은 값을 선택
                    dp[i] = min(dp[i], dp[i - coin] + 1)

            # 만약 dp[amount]가 처음 설정한 큰 값 그대로라면 조합을 만들 수 없다는 뜻으로
            # -1 반환
        return dp[amount] if dp[amount] != amount + 1 else -1
