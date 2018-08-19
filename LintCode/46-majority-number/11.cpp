class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: The majority number
     */
    int majorityNumber(vector<int> nums) {
        // write your code here
        int cnt = 0;
        int last = 0;
        for(int e : nums){
            if(cnt == 0 || last == e){
                last = e;
                cnt++;
            }else{
                cnt--;
            }
        }
        return last;
    }
};
