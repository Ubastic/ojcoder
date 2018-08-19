//min swaps
class Solution {
public:
    int partitionArray(vector<int> &nums, int k) {
        // write your code here
        int left = 0;
        int right = nums.size() - 1;
        
        while (left <= right) {
            while (left <= right && nums[left] < k) {
                ++left;
            } 
            while (left <= right && nums[right] >= k) {
                --right;
            }
            if (left <= right) {
               swap(nums[left++], nums[right--]);
            }
        }
        return left;
    }
};
