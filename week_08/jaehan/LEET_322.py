## 동전 교환

class Solution(object):
    def coinChange(self, coins, amount):

        # 금액을 만들 수 없는 경우를 대비해 무한대 대신 amount + 1로 초기화
        dp = [amount + 1] * (amount + 1)
        
        # 0원을 만드는 데 필요한 동전은 0개
        dp[0] = 0
        
        # 1원부터 amount원까지 차례대로 최소 동전 개수를 구함
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # 최종 금액(amount)을 만드는 것이 불가능하다면 -1 반환, 가능하다면 최소 개수 반환
        return dp[amount] if dp[amount] != amount + 1 else -1