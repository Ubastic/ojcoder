class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minSoFar = INT_MAX;
        int maxProfit = 0;
        for (int n : prices) {
            maxProfit = max(maxProfit, n - minSoFar);
            minSoFar = min(minSoFar, n);
        }
        return maxProfit;
    }
};