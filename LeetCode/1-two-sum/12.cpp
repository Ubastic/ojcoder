class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>::iterator it, start=nums.begin(), it_rem;
        map<int,int> m;
        vector<int> result;
          
        for(it=nums.begin();it!=nums.end();it++){
            int num=*it;
            int rem=target-num;
     
            if(m[rem]==1){
                it_rem=find(nums.begin(), nums.end(), rem);
                result.push_back(it_rem - start);
                result.push_back(it - start);
                return result;
            }
            else{
               m[num]=1;
            }
        }
    }
};
