public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    public int maxTwoSubArrays(ArrayList<Integer> nums) {
        // write your code
        int[] leftMax = new int[nums.size()], rightMax = new int[nums.size()];
        int sum = nums.get(0);
        
        leftMax[0] = nums.get(0);
        int maxVal = nums.get(0);
        
        for(int i = 1; i < nums.size(); i++){
            sum = Math.max(nums.get(i), sum + nums.get(i));
            maxVal = Math.max(maxVal, sum);
            leftMax[i] = maxVal;
        }
        
        sum = nums.get(nums.size() - 1);
        rightMax[nums.size() - 1] = sum;
        maxVal = sum;
        
        for(int i = nums.size() - 2; i >= 0; i--){
            sum = Math.max(nums.get(i), sum + nums.get(i));
            maxVal = Math.max(maxVal, sum);
            rightMax[i] = maxVal;
        }
        
        int ans = Integer.MIN_VALUE;
        
        for(int i = nums.size() - 1; i > 0; i--) ans = Math.max(ans, rightMax[i] + leftMax[i - 1]);
            
        return ans;
    }
}

