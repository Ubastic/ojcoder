class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        if (nums.size() < 2)    return false;
        unordered_set<int> seen;
        seen.insert(0);
        seen.insert(nums[0]);
        int sum = nums[0];
        for (auto i = 1; i != nums.size(); ++i) {
            if (nums[i] == 0 && nums[i-1] == 0)     return true;
            else if (k == 0)    continue;
            else {
                sum = (sum + nums[i]) % k;
                if (seen.find(sum) != seen.end())   return true;
                seen.insert(sum);
            }
            nums[i] = nums[i] % k;
        }
        return false;
    }
};