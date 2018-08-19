class Solution {
public:
    int partitionArray(vector<int> &nums, int k) {
        // write your code here
        int lo = 0;
        int hi = nums.size() - 1;
        
        while(lo <= hi){
            if(nums[lo] < k)
                lo++;
            else
                swap(nums[lo], nums[hi--]);
        }
        return lo;
    }
};
