class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        // write your code here
        vector<int>::iterator it, start=nums.begin(), it_rem;
        map<int,int> m;
        vector<int> result;
          
        for(it=nums.begin();it!=nums.end();it++){
            int num=*it;
            int rem=target-num;
     
            if(m[rem]==1){
                it_rem=find(nums.begin(), nums.end(), rem);
                result.push_back(it_rem - start + 1);
                result.push_back(it - start + 1);
                return result;
            }
            else{
               m[num]=1;
            }
        }
    }
};
