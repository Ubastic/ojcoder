class Solution {
public:    
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    int max(int a, int b)
    {
        return a > b ? a : b;
    }
    int maxSubArray(vector<int> nums) {
        // write your code here
        if(nums.empty())
            return NULL;
        int maxCur = nums[0];
        int maxSoFar = nums[0];
        vector<int>::size_type len = nums.size();
        for(vector<int>::size_type i = 1; i < len; i++)
        {
            maxCur = max(nums[i] , nums[i] + maxCur);//比较当前值与当前值加上前面最大和的大小
            maxSoFar = max(maxSoFar , maxCur);
        }
        return maxSoFar;
    }
};
