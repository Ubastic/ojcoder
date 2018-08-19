class Solution {
public:
    int longestPalindromeSubseq(string s) {
        if (s.empty())  return 0;
        int len = s.size();
        vector<vector<int>> dp(len, vector<int>(len, 1));
        for (int i = len - 1; i >= 0; i--) {
            for (int j = i + 1 ; j < len ; j++) {
                if (s[i] == s[j]) {
                    dp[i][j] = i +1 <= j - 1 ? dp[i+1][j-1] + 2 : 2;
                }
                else {
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        return dp[0][len-1];
    }
};