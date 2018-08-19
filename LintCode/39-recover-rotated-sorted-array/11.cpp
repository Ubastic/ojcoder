class Solution {
public:
    void recoverRotatedSortedArray(vector<int> &nums) {
        // write your code here
        int sz = nums.size();
        if(sz == 0 || sz == 1)
            return;
        int i = 0;
        int j = 1;
        int k = 0;
        for(j = 1; j < sz; j++){
            if(nums[j] < nums[j-1]){
                reverse(nums.begin(), nums.begin() + j);
                reverse(nums.begin() + j, nums.end());
                reverse(nums.begin(), nums.end());
                break;
            }
        }
 /*       
        template <class BidirectionalIterator>
        void reverse (BidirectionalIterator first, BidirectionalIterator last){
            while ((first!=last)&&(first!=--last)) {
                std::iter_swap (first,last);
                ++first;
            }
        }
*/
    }
};
