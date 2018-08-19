public class Solution {
    public int minMoves(int[] nums) {
        if (nums == null || nums.length <= 1)   return 0;
        
        int res = 0;
        int minN = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            minN = Math.min(minN, nums[i]);
        }
        
        for (int i = 0; i < nums.length; i++) {
            res += nums[i] - minN;
        }
        
        return res;
    }
}