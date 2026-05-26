/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    // 1. DP 배열을 만들고, 만들 수 없는 최댓값(amount + 1)으로 초기화
    const dp = new Array(amount + 1).fill(amount + 1);
    
    // 2. 0원을 만드는 최소 동전 개수는 0개
    dp[0] = 0;

    // 3. 1원부터 목표 금액(amount)까지 최소 동전 개수를 차례대로 구함
    for (let i = 1; i <= amount; i++) {
        for (let coin of coins) {
            // 현재 구하려는 금액(i)이 동전의 액면가보다 크거나 같을 때만 뺄 수 있음
            if (i - coin >= 0) {
                // 기존에 저장된 최소 개수와 (현재 동전을 뺀 금액의 최소 개수 + 1) 중 더 작은 값을 저장
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    // 4. 최종 목표 금액에 도달할 수 없다면(초기값이 그대로라면) -1을 반환, 아니면 계산된 최솟값을 반환
    return dp[amount] === amount + 1 ? -1 : dp[amount];
};
