class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_set<int> us;
        vector<int> res;
        for (auto n : nums) {
            if (us.find(n) != us.cend()) {
                res.push_back(n);
            } else {
                us.insert(n);
            }
        }
        return res;
    }
};