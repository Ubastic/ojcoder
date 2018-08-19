public class Solution {
    int count;
    public int findTargetSumWays(int[] nums, int S) {
        count = 0;
        helper(nums, S, 0, 0);
        return count;
    }
    private void helper(int[] nums, int S, int s, int i) {
        if (i == nums.length) {
            if (S == s) {
                count++;
            }
            return;
        }
        helper(nums, S, s + nums[i], i + 1);
        helper(nums, S, s - nums[i], i + 1);
    }
}