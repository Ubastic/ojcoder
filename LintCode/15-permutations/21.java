/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/permutations
@Language: Java
*/

class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    private HashMap<List<Integer>, List<Integer>> helper(HashMap<List<Integer>, List<Integer>> M){
        HashMap<List<Integer>, List<Integer>> newM = new HashMap<>();
        
        for(Map.Entry<List<Integer>, List<Integer>> e : M.entrySet()){
            for(int i = 0; i < e.getValue().size(); i++){
                List<Integer> newKey = new ArrayList<>(e.getKey()), newValue = new ArrayList<>(e.getValue());
                
                newKey.add(e.getValue().get(i));
                newValue.remove(i);
                newM.put(newKey, newValue);
            }
        }
        
        return newM;
    }
    
    public List<List<Integer>> permute(int[] nums) {
        // write your code here
        List<List<Integer>> ans = new ArrayList<>();
        
        if(nums == null || nums.length == 0){
            ans.add(new ArrayList<Integer>());
            
            return ans;
        }
        
        HashMap<List<Integer>, List<Integer>> M = new HashMap<>();
        List<Integer> l = new ArrayList<>();
        
        for(int num : nums) l.add(num);
        
        M.put(new ArrayList<Integer>(), l);
        
        for(int i = 0; i < nums.length; i++) M = helper(M);
        
        for(List<Integer> k : M.keySet()) ans.add(k);
        
        return ans;
    }
}
