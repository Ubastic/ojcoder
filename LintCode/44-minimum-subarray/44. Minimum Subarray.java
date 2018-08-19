public class Solution {
    /**
     * @param nums: a list of integers
     * @return: A integer indicate the sum of minimum subarray
     */
    public int minSubArray(ArrayList<Integer> nums) {
        // write your code
        if(nums == null || nums.size() == 0) return 0;
        
        int sum = nums.get(0), minSum = sum;
        
        for(int i = 1; i < nums.size(); i++){
            sum = Math.min(nums.get(i), nums.get(i) + sum);
            minSum = Math.min(minSum, sum);
        }
        
        return minSum;
    }
}
