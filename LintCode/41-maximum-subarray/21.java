public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    public int maxSubArray(int[] nums) {
        // write your code
        int max_ending_here = nums[0];
        int max_so_far = nums[0];
        for( int i =1 ;i<nums.length; i++) {
            max_ending_here = Math.max( nums[i] , nums[i] + max_ending_here );
            max_so_far = Math.max( max_so_far, max_ending_here);
        }
        return max_so_far;
    }
}
