class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    int maxTwoSubArrays(vector<int> nums) {
        // write your code here
        int sz = nums.size();
        if(sz < 2)
            return -1;

        int mx1[sz]; // mx1[i] means the max subarray before ending at index i
        mx1[0] = nums[0];
        int sum = 0;
	    int mx2 = nums[sz - 1];
	    int mx = mx1[0] + mx2; 
        for(int i = 0; i < sz; i++){
            sum += nums[i];
            mx1[i] = max(i==0 ? sum:mx1[i-1], sum);//record the max subarray before index i(included)
            sum = sum<0 ? 0:sum;
	    }

        sum = 0;
        for(int j = sz - 1; j > 0 ; j--){
            sum += nums[j];
            mx2 = max(mx2, sum); //record the max subarray after index j(included)
            sum = sum<0 ? 0:sum;
            mx = max(mx, mx1[j-1] + mx2); //find the max sum of two subarray break at index j([0,j-1] , [j, sz-1])
        }
        return mx;
    }
};
