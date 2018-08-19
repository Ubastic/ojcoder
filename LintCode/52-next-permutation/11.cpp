class Solution {
public:
    /**
     * @param nums: An array of integers
     * @return: An array of integers that's next permuation
     */
    vector<int> nextPermutation(vector<int> &nums) {
        // write your code here
        int sz = nums.size();
        int i = sz - 2;
        int j = sz - 1;
        
        while(i>=0 && nums[i] >= nums[i+1])
            i--;
        if(i == -1){
            reverse(nums.begin(), nums.end());
            return nums;
        }
        
        while(j>=0 && nums[j] <= nums[i])
            j--;
            
        swap(nums[i], nums[j]);
        reverse(nums.begin() + i + 1, nums.end());
        return nums;
    }
};
