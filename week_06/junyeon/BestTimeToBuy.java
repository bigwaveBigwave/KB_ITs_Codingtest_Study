package week_06.junyeon;

public class BestTimeToBuy {
    public int maxProfit(int[] prices) {
        int answer = 0;
        for (int i = 0 ; i < prices.length - 1 ; i++) {
            if (prices[i+1] - prices[i] > 0) {
                answer += prices[i+1] - prices[i];
            }
        }

        return answer;
    }
}
