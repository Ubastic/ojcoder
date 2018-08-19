class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty())  return 0;
        vector<int> prev{costs[0][0], costs[0][1], costs[0][2]};
        vector<int> curr{0, 0, 0};
        for (int i = 0; i != costs.size() - 1; ++i) {
            curr[0] = min(prev[1], prev[2]) + costs[i+1][0];
            curr[1] = min(prev[0], prev[2]) + costs[i+1][1];
            curr[2] = min(prev[1], prev[0]) + costs[i+1][2];
            prev = curr;
        }
        return *min_element(begin(prev), end(prev));
    }
};