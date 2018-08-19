public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer indicate the value of maximum difference between two
     *          Subarrays
     */
    public int maxDiffSubArrays(int[] nums) {
        // write your code here
        int[] leftMax = new int[nums.length], leftMin = new int[nums.length], rightMax = new int[nums.length], rightMin = new int[nums.length];
        int sum1 = nums[0], sum2 = nums[0], minSum = nums[0], maxSum = nums[0];
        
        leftMin[0] = nums[0];
        leftMax[0] = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            sum1 = Math.min(nums[i], sum1 + nums[i]);
            sum2 = Math.max(nums[i], sum2 + nums[i]);
            minSum = Math.min(minSum, sum1);
            maxSum = Math.max(maxSum, sum2);
            leftMin[i] = minSum;
            leftMax[i] = maxSum;
        }
        
        sum1 = nums[nums.length - 1];
        sum2 = nums[nums.length - 1];
        minSum = sum1;
        maxSum = sum2;
        rightMin[nums.length - 1] = sum1;
        rightMax[nums.length - 1] = sum2;
        
        for(int i = nums.length - 2; i >= 0; i--){
            sum1 = Math.min(nums[i], sum1 + nums[i]);
            sum2 = Math.max(nums[i], sum2 + nums[i]);
            minSum = Math.min(minSum, sum1);
            maxSum = Math.max(maxSum, sum2);
            rightMin[i] = minSum;
            rightMax[i] = maxSum;
        }
        
        int ans = 0;
        
        for(int i = nums.length - 1; i > 0; i--){
            ans = Math.max(ans, Math.abs(leftMax[i - 1] - rightMin[i]));
            ans = Math.max(ans, Math.abs(leftMin[i - 1] - rightMax[i]));
        }
        
        return ans;
    }
}

