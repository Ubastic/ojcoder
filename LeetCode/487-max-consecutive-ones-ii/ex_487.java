public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0, left = 0, right = 0;
        for (int n : nums) {
            right++;
            if (n == 0) {
                left = right;
                right = 0;
            }
            maxCount = Math.max(maxCount, left + right);
        }
        return maxCount;
    }
}