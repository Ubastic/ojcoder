/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/permutations-ii
@Language: Java
*/

class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of unique permutations.
     */
    private void swap(List<Integer> l, int x, int y){
        int tmp = l.get(x);
        l.set(x, l.get(y));
        l.set(y, tmp);
    } 
    
    private void helper(List<List<Integer>> resSet, List<Integer> l, int start, int end){
        if(start == end){
            resSet.add(l);
            return;
        }
        
        helper(resSet, l, start + 1, end);
        
        for(int i = start + 1; i <= end; i++){
            if(l.get(i) == l.get(start) || l.get(i) == l.get(i - 1)) continue;
            
            List<Integer> newL = new ArrayList<>(l);
            
            swap(newL, start, i);
            helper(resSet, newL, start + 1, end);
        }
    }
    
    public List<List<Integer>> permuteUnique(int[] nums) {
        // Write your code here
        List<List<Integer>> ans = new ArrayList<>();
        
        if(nums == null || nums.length == 0){
            ans.add(new ArrayList<Integer>());
            
            return ans;
        }
        
        Arrays.sort(nums);
        
        List<Integer> l = new ArrayList<>();
        
        for(int num : nums) l.add(num);
        
        helper(ans, l, 0, nums.length - 1);
        
        return ans;
    } 
}


