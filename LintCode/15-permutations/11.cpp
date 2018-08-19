/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/permutations
@Language: C++
*/

//Recursion
class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    vector<vector<int> > permute(vector<int> nums) {
        // write your code here
        vector<vector<int> > res;
        permuteHelper(nums, 0, res);
        return res;
    }
    
    void permuteHelper(vector<int> &nums, int start, vector<vector<int> > &res){
        int sz = nums.size();
        if(start == sz){
            if(sz != 0)
                res.push_back(nums);
            return;
        }
        
        for(int i = start; i < sz; i++){
            swap(nums[start], nums[i]);
            permuteHelper(nums, start+1, res);
            swap(nums[i], nums[start]);
        }
    }
};
