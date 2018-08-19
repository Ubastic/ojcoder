class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        for (auto lo = n; lo > 0; --lo) {
            for (auto hi = lo+1; hi < n+1; ++hi) {
                dp[lo][hi] = 0x7fffffff;
                for (auto i = lo; i < hi; ++i) {
                    dp[lo][hi] = min(dp[lo][hi], i + max(dp[i+1][hi], dp[lo][i-1]));
                }
            }
        }
        return dp[1][n];
    }
};