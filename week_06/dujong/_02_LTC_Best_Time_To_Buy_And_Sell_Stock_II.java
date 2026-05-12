class Solution {
    public int maxProfit(int[] prices) {
        // 현재 숫자가 이전 숫자보다 커지는 경우 -> 해당 차이 만큼 수익 내기
        int profit = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
        }

        return profit;
    }
}
