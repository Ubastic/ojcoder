public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        if (nums.length < 3)  return 0;
        int count = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; ++i) {
            int tar = target - nums[i];
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                if (nums[j] + nums[k] < tar) {
                    count += k - j;
                    j++;
                }
                else    k--;
            }
        }
        return count;
    }
}