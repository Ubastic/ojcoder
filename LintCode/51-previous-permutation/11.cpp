class Solution {
public:
    /**
     * @param nums: An array of integers
     * @return: An array of integers that's previous permuation
     */
    vector<int> previousPermuation(vector<int> &nums) {
        // write your code here
        int sz = nums.size();
        int i = sz - 2;
        while(i >=0 && nums[i] <= nums[i+1])
            i--;

        if (i == -1){
            reverse(nums.begin(), nums.end());
            return nums;
        }
        
        int j = sz - 1;
        while(j > i && nums[j] >= nums[i])
            j--;
        
        swap(nums[i], nums[j]);
        reverse(nums.begin() + i + 1, nums.end());
        return nums;
    }
};
