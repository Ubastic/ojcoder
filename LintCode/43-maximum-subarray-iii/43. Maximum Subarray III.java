public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: An integer denote to find k non-overlapping subarrays
     * @return: An integer denote the sum of max k non-overlapping subarrays
     */
     
    public int maxSubArray(int[] nums, int k) {
        // write your code here
        if(nums == null || nums.length == 0 || k == 0) return 0;
        
        int[][] global = new int[nums.length + 1][k + 1], local = new int[nums.length + 1][k + 1];
        
        for(int i = 1; i <= k; i++){
            local[i - 1][i] = Integer.MIN_VALUE;
            for(int j = i; j <= nums.length; j++){
                local[j][i] = Math.max(local[j - 1][i], global[j - 1][i - 1]) + nums[j - 1];
                global[j][i] = i == j ? local[j][i] : Math.max(global[j - 1][i], local[j][i]);
            }
        }
        
        return global[nums.length][k];
    }
}
