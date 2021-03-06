class Solution {
public:
    /**
     * @param nums: A list of integers
     * @param k: As described
     * @return: The majority number
     */
    int majorityNumber(vector<int> nums, int k) {
        // write your code here
        int sz = nums.size();
        unordered_map<int, int> mp;
        for(int i = 0; i < sz; i++){
            if(mp.find(nums[i]) == mp.end()){
                if(mp.size() == k-1){
                    for(auto it = mp.begin(); it != mp.end(); it++){
                        it->second--;
                        if(it->second == 0)
                            mp.erase(it->first);   
                    }
                }else {
                    mp[nums[i]] = 1;
                }
            }else{
                mp[nums[i]]++;
            }    
        }

        for(int i = 0; i < sz; i++){
            if(mp.find(nums[i]) != mp.end()){
                if(mp[nums[i]] >= 0)
                    mp[nums[i]] = -1;
                else
                    mp[nums[i]]--;
                if(-mp[nums[i]] > sz/k)
                    return nums[i];
            }
        }
        return -1;
    }
};

class Solution {
public:
    /**
     * @param nums: A list of integers
     * @param k: As described
     * @return: The majority number
     */
    int majorityNumber(vector<int> nums, int k) {
        // write your code here
        int sz = nums.size();
        unordered_map<int, int> mp;
        for(int i = 0; i < sz; i++){
            if(mp.find(nums[i]) == mp.end()){
                if(mp.size() == k-1){
                    for(auto it = mp.begin(); it != mp.end(); it++){
                        it->second--;
                        if(it->second == 0)
                            mp.erase(it->first);   
                    }
                }else {
                    mp[nums[i]] = 1;
                }
            }else{
                mp[nums[i]]++;
            }    
        }

        for(auto it = mp.begin(); it != mp.end(); it++)
            it->second = 0;

        for(int i = 0; i < sz; i++){
            if(mp.find(nums[i]) != mp.end() && (++mp[nums[i]] > sz/k))
                return nums[i];
        }
        return -1;
    }
};
