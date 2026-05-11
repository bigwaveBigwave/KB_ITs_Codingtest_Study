class Solution {
    public int maxProfit(int[] prices) {
        int total = 0;
        int len = prices.length;

        int i = 0;

        while (i < len-1) {
            int todayPrice = prices[i];
            int tomorrowPrice = prices[i+1];

            if(todayPrice < tomorrowPrice) {
                total += (tomorrowPrice - todayPrice);
            }
            
            i++;
        }

        return total;
    }
}