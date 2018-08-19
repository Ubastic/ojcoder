public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    public int maxSubArray(int[] nums) {
        // write your code
        if(nums == null || nums.length == 0) return 0;
        
        int maxSum = nums[0], sum = nums[0] < 0 ? nums[0] : 0;
        
        for(int num : nums){
            if(num < 0) maxSum = Math.max(maxSum, sum);
            
            sum = Math.max(num, sum + num);
        }
        
        maxSum = Math.max(maxSum, sum);
        
        return maxSum;
    }
}
