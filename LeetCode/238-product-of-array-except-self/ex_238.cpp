class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        int product = 1;
        for (auto &i : nums) {
            res.push_back(product);
            product *= i;
        }
        product = 1;
        for (int i = nums.size() - 2; i >= 0; --i) {
            product *= nums[i + 1];
            res[i] *= product;
        }
        return res;
    }
};