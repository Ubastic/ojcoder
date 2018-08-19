public class Solution {
    public int getMoneyAmount(int n) {
        int[][] dp = new int[n+1][n+1];
        for (int lo = n; lo > 0; lo--) {
            for (int hi = lo + 1; hi < n + 1; hi++) {
                dp[lo][hi] = 0x7fffffff;
                for (int i = lo; i < hi; i++) {
                    dp[lo][hi] = Math.min(dp[lo][hi], i + Math.max(dp[i+1][hi], dp[lo][i-1]));    
                }
            }
        }
        return dp[1][n];
    }
}