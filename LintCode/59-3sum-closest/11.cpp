class Solution {
public:    
    /**
     * @param numbers: Give an array numbers of n integer
     * @param target: An integer
     * @return: return the sum of the three integers, the sum closest target.
     */
    int threeSumClosest(vector<int> nums, int target) {
        // write your code here
        int sz = nums.size();
        int res = INT_MAX;
        int diff = INT_MAX;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < sz - 2; i++){
            int j = i + 1;
            int k = sz -1;
            while(j < k){
                int sum = nums[i] + nums[j] + nums[k];
                int delta = abs(sum - target);
                if(delta < diff){
                    diff = delta;
                    res = sum;
                    if(delta == 0)
                        return res;
                }
                if(sum > target)
                    k--;
                else
                    j++;
            }
        }
        return res;
    }
};
