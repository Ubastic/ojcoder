/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/permutations-ii
@Language: C++
*/

class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of unique permutations.
     */
    vector<vector<int> > permuteUnique(vector<int> &nums) {
        // write your code here
        vector<int> visited(nums.size(),0);
        vector<int> out;
        set<vector<int> > res;
        //sort(num.begin(), num.end());
        permuteUniqueDFS(nums, 0, visited, out, res);
        return vector<vector<int> >(res.cbegin(),res.cend());
    }
    
    void permuteUniqueDFS(vector<int> &nums, int level, vector<int> &visited, vector<int> &out, set<vector<int> > &res){
        if(level == nums.size()){
            res.insert(out);
            return;
        }
        for(int i = 0; i < nums.size() ; i++){
            if(!visited[i]){
                if (i > 0 && nums[i] == nums[i - 1] && visited[i - 1] == 0) continue;
                visited[i] = 1;
                out.push_back(nums[i]);
                permuteUniqueDFS(nums, level + 1, visited, out, res);
                out.pop_back();
                visited[i] = 0;
            }
        }
    }
};