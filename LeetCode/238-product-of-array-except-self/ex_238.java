public class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int product = 1, idx = 0;
        for (int i : nums) {
            res[idx++] = product;
            product *= i;
        }
        product = 1;
        for (int i = nums.length - 2; i >= 0; --i) {
            product *= nums[i + 1];
            res[i] *= product;
        }
        return res;
    }
}