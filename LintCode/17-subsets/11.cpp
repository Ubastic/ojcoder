/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/subsets
@Language: C++
*/

class Solution {
public:
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    vector<vector<int> > subsets(vector<int> &nums) {
    	// write your code here
    	int n = nums.size();
    	int mx = 1 << n;
    	vector<vector<int> > res;
    	sort(nums.begin(), nums.end());//need sort to make sure the order is correct
    	for(int i = 0; i < mx; i++){
    	    vector<int> sol;
    	    for(int shift = 0; shift < n; shift++){
    	        if((i>>shift) & 0x1){
    	            sol.push_back(nums[shift]);
    	        }
    	    }
    	    res.push_back(sol);
    	}
    	return res;
    }
};
