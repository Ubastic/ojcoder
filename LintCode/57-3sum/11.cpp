class Solution {
public:    
    /**
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    vector<vector<int> > threeSum(vector<int> &nums) {
        // write your code here
        int sz = nums.size();
        vector<vector<int> > res;
        sort(nums.begin(), nums.end());

        for(int i = 0; i < sz; i++){
            if(nums[i] > 0)
                return res;
            if(i>0 && nums[i] == nums[i-1])
                continue;

            int a = i + 1;
            int b = sz -1;
            int target = -nums[i];

            while(a < b){
                if(a>i+1 && nums[a] == nums[a-1]){
                    a++;
                    continue;
                }
                if(b<sz-1 && nums[b] == nums[b+1]){
                    b--;
                    continue;
                }
                    
                vector<int> sol;
                if(nums[a] + nums[b] == target){
                    sol.push_back(nums[i]);
                    sol.push_back(nums[a]);
                    sol.push_back(nums[b]);
                    res.push_back(sol);
                    a++;
                    b--;
                }else if(nums[a] + nums[b] > target){
                    b--;
                }else{
                    a++;
                }
            }
        }
        return res;
    }
};
