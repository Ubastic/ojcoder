//O(n) Space, O(n) Time
class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        // write your code here
        unordered_map<int, int> mp;
        vector<int> res;
        int sz = nums.size();
        for(int i=0; i<sz; i++){
            if(mp.find(nums[i]) == mp.end()){
                mp[target - nums[i]] = i;
            }else{
                res.push_back(1 + min(mp[nums[i]], i));
                res.push_back(1 + max(mp[nums[i]], i));
            }
        }
        return res;
    }
};

