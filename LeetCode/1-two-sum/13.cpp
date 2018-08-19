class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dict;
        vector<int> res;
        for (size_t i = 0; i != nums.size(); ++i) {
            if (dict.find(target - nums[i]) != dict.end()) {
                res.push_back(dict[target - nums[i]]);
                res.push_back(i);
                break;
            }
            dict[nums[i]] = i;
        }
        return res;
    }
};