class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<string> res;
        nums.push_back(upper + 1);
        int pre = lower - 1;
        for (auto &i : nums) {
            if (i == pre + 2)   res.push_back(to_string(i-1));
            if (i > pre + 2)    res.push_back(to_string(pre+1) + "->" + to_string(i-1));
            pre = i;
        }
        return res;
    }
};