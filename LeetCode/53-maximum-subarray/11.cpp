const int INF = 1 << 31;
class Solution {
public:
    inline int max(int a, int b)
    {
        return a > b ? a : b;
    }
    int maxSubArray(vector<int>& nums) {
        vector<int>::size_type len = nums.size();
        if(len == 0)
            return -INF;
        int maxCur = nums[0];
        int maxSoFar = nums[0];
        for(vector<int>::size_type i = 1; i < len; i++)
        {
            maxCur = max(nums[i] , nums[i] + maxCur);//比较当前值与当前值加上前面最大和的大小
            maxSoFar = max(maxSoFar , maxCur);
        }
        return maxSoFar;
    }
};
