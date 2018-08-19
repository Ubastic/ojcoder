/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/permutations
@Language: C++
*/

class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    vector<vector<int> > permute(vector<int> nums) {
        // write your code here
        vector<int> visited(nums.size(),0);
        vector<int> out;
        vector<vector<int> > res;
        permuteDFS(nums, 0, visited, out, res);
        return res;
    }
    
    void permuteDFS(vector<int> &nums, int level, vector<int> &visited, vector<int> &out, vector<vector<int> > &res){
        if(level == nums.size()){
            res.push_back(out);
            return;
        }
        for(int i = 0; i < nums.size() ; i++){
            if(!visited[i]){
                visited[i] = 1;
                out.push_back(nums[i]);
                permuteDFS(nums, level + 1, visited, out, res);
                out.pop_back();
                visited[i] = 0;
            }
        }
    }
};
