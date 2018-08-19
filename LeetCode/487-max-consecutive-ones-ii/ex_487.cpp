class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_count = 0, left = 0, right = 0;
        for (auto &n : nums) {
            ++right;
            if (n == 0) {
                left = right;
                right = 0;
            }
            max_count = max(max_count, left + right);
        }
        return max_count;
    }
};