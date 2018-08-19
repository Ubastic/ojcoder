public class Solution {
    public int maxProfit(int[] prices) {
        int minSoFar = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int n : prices) {
            maxProfit = Math.max(maxProfit, n - minSoFar);
            minSoFar = Math.min(minSoFar, n);
        }
        return maxProfit;
    }
}