class 주식판매 {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int n = prices.length;

        for (int i = 1; i < n; i++) {
            if (prices[i] > prices[i - 1]) {
                maxProfit += prices[i] - prices[i - 1];
            }
        }
        return maxProfit;
    }
}