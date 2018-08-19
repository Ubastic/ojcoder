/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/subsets
@Language: Java
*/

class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    private void helper(ArrayList<ArrayList<Integer>> resSet, ArrayList<Integer> l, int[] nums, int start, int k){
        if(k == 0){
            resSet.add(new ArrayList<Integer>(l));
            return;
        }
        
        for(int i = start; i < nums.length; i++){
            l.add(nums[i]);
            helper(resSet, l, nums, i + 1, k - 1);
            l.remove(l.size() - 1);
        }
    }
    
    public ArrayList<ArrayList<Integer>> subsets(int[] nums) {
        // write your code here
        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<Integer>());
        
        if(nums == null || nums.length == 0) return ans;
        
        Arrays.sort(nums);
        
        for(int i = 1; i <= nums.length; i++) helper(ans, new ArrayList<Integer>(), nums, 0, i);
        
        return ans;
    }
}
