public class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int res = (n + 1) * n / 2;
        for (int i : nums)
            res -= i;
        return res;
    }
}