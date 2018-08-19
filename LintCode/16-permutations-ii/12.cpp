/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/permutations-ii
@Language: C++
*/

//Recursion
class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of unique permutations.
     */
    vector<vector<int> > permuteUnique(vector<int> &nums) {
        // write your code here
        vector<vector<int> > res;
        permuteUniqueHelper(nums, 0, res);
        return res;
    }
    
    void permuteUniqueHelper(vector<int> &nums, int start, vector<vector<int> > &res){
        int sz = nums.size();
        if(start == sz){
            if(sz != 0)
                res.push_back(nums);
            return;
        }
        
        for(int i = start; i < sz; i++){
            if(do_swap(nums, start, i)){
                swap(nums[start], nums[i]);
                permuteUniqueHelper(nums, start+1, res);
                swap(nums[i], nums[start]);
            }
        }
    }
    
    bool do_swap(vector<int>&nums, int start, int end){
        while(start < end){
            if(nums[start++] == nums[end])
                return false;
        }
        return true;
    }
};
