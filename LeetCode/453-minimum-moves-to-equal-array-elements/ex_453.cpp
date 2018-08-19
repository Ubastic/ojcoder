class Solution {
public:
    int minMoves(vector<int>& nums) {
        int res = 0;
        int min_n = *min_element(nums.cbegin(), nums.cend());
        for (int n : nums) {
            res += n - min_n;
        }
        return res;
    }
};