class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int count = 0;
        helper(nums, S, count, 0, 0);
        return count;
    }
private:
    void helper(vector<int>& nums, int S, int& count, int s, int i) {
        if (i == nums.size()) {
            if (S == s) {
                ++count;
            }
            return;
        }
        helper(nums, S, count, s + nums[i], i + 1);
        helper(nums, S, count, s - nums[i], i + 1);
    }
};