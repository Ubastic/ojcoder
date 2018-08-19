class Solution {
public:    
    /**
	 * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    int maxSubArray(vector<int> nums) {
        // write your code here
        int sz = nums.size();
        if(sz ==0)
            return 0;
        int sum = 0;
        int mx = nums[0];
        for(int e : nums){
            sum+=e;
            mx = sum>mx ? sum:mx;
            sum = sum<0 ? 0:sum;
        }
        return mx;
    }
};
