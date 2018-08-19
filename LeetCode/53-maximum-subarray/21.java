public class Solution {
    public int maxSubArray(int[] nums) {
        int maxSofar = nums[0];
            int maxCur = nums[0];
            for(int i=1; i<nums.length;i++)
            {              
                maxCur = Math.max(nums[i], nums[i] + maxCur);
                maxSofar = Math.max(maxCur, maxSofar);
            }
            return maxSofar;
    }
}
